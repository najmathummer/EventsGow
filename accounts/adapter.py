from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.forms import ValidationError



class DefaultAccountAdapterCustom(DefaultAccountAdapter):

    def clean_email(self, email):
        email = super().clean_email(email)
        if "gla.ac.uk" not in email.split('@')[1]:
            print(email.split('@')[1])
            raise ValidationError("Please use university email address")
        # if email_has_banned_domain(email):
        #     raise forms.ValidationError("Your domain is bad.")

        return email
