from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm



class MyCustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class': 'form-control '})
        self.fields['password'].widget.attrs.update({'class': 'form-control '})
    def login(self, *args, **kwargs):
        return super(MyCustomLoginForm, self).login(*args, **kwargs)
    
class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control '})
        self.fields['username'].widget.attrs.update({'class': 'form-control '})
        self.fields['password1'].widget.attrs.update({'class': 'form-control '})
        self.fields['password2'].widget.attrs.update({'class': 'form-control '})
    
    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        return user

class MyCustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control '})
    
    def save(self, request):

        email_address = super(MyCustomResetPasswordForm, self).save(request)
        return email_address

