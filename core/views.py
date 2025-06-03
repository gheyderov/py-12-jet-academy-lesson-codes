from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from product.models import ProductCategory
from core.forms import ContactForm
from django.contrib import messages

# Create your views here.


def homepage(request):
    return render(request, 'index.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        print(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            messages.add_message(request, messages.SUCCESS, "Message was sent successfully!")
            return redirect(reverse_lazy('contact'))
        
    context = {
        'form' : form
    }
    return render(request, 'contact.html', context)

def about(request):
    return render(request, 'about.html')