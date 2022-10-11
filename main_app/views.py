from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from .models import Project

def home(request):
    # Handle list of reference projects.
    projects = Project.objects.all()[:5]

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
    
    return render(request, 'home.html', context={'form': form, 'projects': projects})

def contact_sucess_view(request):
    return render(request, 'contact_success.html', context={})