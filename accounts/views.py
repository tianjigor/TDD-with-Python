from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from accounts.models import Token
from django.core.urlresolvers import reverse
# Create your views here.

def send_login_email(request):
    email = request.POST['email']
    Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(Token.uid)
    )
    message_body = 'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for Superlists',
        message_body,
        'noreply@superlists',
        [email]
    )

    # print (type(send_mail))
    #
    # send_mail(
    #     'Your login link for Superlists',
    #     'Use this link to log in',
    #     'noreply@superlists',
    #     [email],
    # )

    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )

    # messages.add_message(
    #     request,
    #     messages.SUCCESS,
    #     "Check your email, we've sent you a link you can use to log in."
    # )

    return redirect('/')


def login(request):
    return redirect('/')


