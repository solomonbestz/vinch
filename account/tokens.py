from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type
from .models import NewUser


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: NewUser, timestamp):
        return(
            text_type(user.pk) + text_type(timestamp) +
            text_type(user.newuser.is_active)
        )
    
account_activation_token = AccountActivationTokenGenerator()