from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from account.forms import RegisterForm, LoginForm, ProfileForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required

# Create your views here.

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
        print(request.POST)
        if form.is_valid():
            form.save(commit=False)
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


