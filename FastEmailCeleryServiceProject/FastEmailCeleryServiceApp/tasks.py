from celery import shared_task
from celery.utils.log import get_task_logger
import time
from django.core.mail import send_mail
from django.conf import settings
logger=get_task_logger(__name__)

@shared_task
def add(x,y):
    logger.info("Addition Done Successfully")
    return x+y

@shared_task
def sleepy(duration):
    logger.info(f"Sleeping for {duration} seconds")
    time.sleep(duration)
    return None

@shared_task
def send_email_task():
    email_subject="Hello"
    email_body="Hello There How you doing"
    
    send_mail(
        email_subject,
        email_body,
        settings.DEFAULT_EMAIL_FROM,
        ["psarangi50@gmail.com",]
    )
    
    logger.info("Email Sent Successfully")