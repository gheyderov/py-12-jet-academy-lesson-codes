from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from account.forms import RegisterForm

# Create your views here.

def login(request):
    return render(request, 'login.html')


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data = request.POST, files=request.FILES)
        print(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(reverse_lazy('register'))
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)