from sendemailtomyemail.models import Contactus
import time
from django.core.mail import send_mail
from django.conf import settings
import random

def run_this_function():
    print('function_started........')
    time.sleep(2)
    print("function Executed")


def send_email_to_client(email):
    subject = "This is from django server"
    otp = random.randint(10000, 100000)
    message = f"this is a test message from djngaao server {otp}"
    from_email = settings.EMAIL_HOST_USER 
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list, fail_silently=False)
    return otp




