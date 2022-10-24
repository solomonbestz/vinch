from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from .email import send_message
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token


def activate_account(request, user, email):
    current_site = get_current_site(request)
    subject = 'Activate Your Account'
    message = render_to_string('account/account_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user=user),
    })
    send_message(subject,message,email)