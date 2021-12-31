from django.shortcuts import render,HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.

def index(request, *args, **kwargs):
    context={"name":"Rika"}
    email_subject="Hello There"
    email_body=render_to_string("templateEmailApp/email.txt",context)
    email=EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_EMAIL_FROM,
        ["psarangi50@gmail.com",])
    email.send()
    return HttpResponse("Message Been Sent")