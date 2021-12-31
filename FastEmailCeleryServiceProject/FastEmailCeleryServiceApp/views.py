from django.shortcuts import render,HttpResponse
import time

from .tasks import sleepy, add,send_email_task
# Create your views here.

#case:1
#------------------
# def index(request, *args, **kwargs):
#     time.sleep(10)
#     return HttpResponse("<h1> Done Without Celery</h1>")

#case:2
#--------------------
# def index(request, *args, **kwargs):
#     sleepy.delay(10)
#     return HttpResponse("<h1> Done with Celery</h1>")

#case:3
#---------------------
# def index(request, *args, **kwargs):
#     add.delay(10,40)
#     return HttpResponse(f"<h1> Addition with Celery</h1>")

#case:-4:
# ----------------------------------------------------------------

def index(request, *args, **kwargs):
    send_email_task.delay()
    return HttpResponse(f"<h1> Email  Celery</h1>")

