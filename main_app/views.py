from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

def home(request):
    # Handle contact form.
    if request.method == 'GET':
        form = ContactForm
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            try:
                send_mail(f'From: {name}, subject: {subject}', message, from_email, ['johannilsso0@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            
            return redirect('contact_success')
    
    return render(request, 'home.html', context={'form': form})

def contact_sucess_view(request):
    return render(request, 'contact_success.html', context={})