from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.forms import ValidationError



class DefaultAccountAdapterCustom(DefaultAccountAdapter):
    # check whether the email domain is university domain
    def clean_email(self, email):
        email = super().clean_email(email)
        if "gla.ac.uk" not in email.split('@')[1]:
            print(email.split('@')[1])
            raise ValidationError("Please use university email address")

        return email

    def send_mail(self, template_prefix, email, context):
        if 'key' in context:
            context['activate_url'] = settings.BASE_URL + 'accounts/confirm-email/' + context['key']
        elif 'password_reset_url' in context:
            
            context['password_reset_url'] = settings.BASE_URL + 'accounts/password/reset/key/'+ context['password_reset_url'].split('/')[7] + '/'

        msg = self.render_mail(template_prefix, email, context)
        msg.send()

