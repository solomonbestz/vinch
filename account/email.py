from core import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
import datetime 


def send_message(email_subject, email_body, user_email):
    from_email = settings.EMAIL_HOST_USER
    to_user_list = [user_email]
    mail = email_body
    send_mail(email_subject, mail, from_email, to_user_list)