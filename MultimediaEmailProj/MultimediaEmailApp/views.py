from django.shortcuts import render,HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def index(request, *args, **kwargs):
    context={"name":"rika"}
    html_tags=render_to_string("MultimediaEmailApp/email.html",context)
    text_body=strip_tags(html_tags)
    email_subject="hello"
    email=EmailMultiAlternatives(
        
        email_subject,
        text_body,
        settings.DEFAULT_EMAIL_FROM,
        ["psarangi50@gmail.com"]
        
    )
    email.attach_alternative(html_tags,"text/html")
    email.send()
    return HttpResponse("Message Sent")

# def index(request, *args, **kwargs):
#     # context={"name":"rika"}
#     # html_tags=render_to_string("MultimediaEmailApp/email.html",context)
#     # text_body=strip_tags(html_tags)
#     email_subject="hello"
#     text_body="Hello there"
#     email=send_mail(
        
#         email_subject,
#         text_body,
#         settings.DEFAULT_EMAIL_FROM,
#         ["psarangi50@gmail.com",]
        
#     )
#     # email.attach_alternative(html_tags,"text/html")
#     # email.send()
#     return HttpResponse("Message Sent")