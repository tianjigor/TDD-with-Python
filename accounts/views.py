from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
def send_login_email(request):
    email = request.POST['email']
    print (type(send_mail))
    send_mail(
        'Your login link for Superlists',
        'body text tbc',
        'noreply@superlists',
        [email],
    )
    return redirect('/')