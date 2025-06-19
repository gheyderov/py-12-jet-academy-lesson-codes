from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from account.forms import RegisterForm, LoginForm, ProfileForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required

from account.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string

from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.views import LoginView

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm
    

def login(request):
    next = request.GET.get('next', reverse_lazy('home'))
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if not user:
                pass
                # message
            else:
                django_login(request, user)
                return redirect(next)
    context = {
        'form' : form
    }
    return render(request, 'login.html', context)


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data = request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            current_site = get_current_site(request)
            subject = 'Activate Your E-Commerce Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect(reverse_lazy('register'))
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)


def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('login'))

@login_required(login_url='login')
def profile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(data = request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    context = {
        'form' : form
    }
    return render(request, 'profile.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        django_login(request, user)
        return redirect('login')
    else:
        return render(request, 'account_activation_invalid.html')