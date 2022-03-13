from allauth.account.forms import LoginForm
class MyCustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class': 'form-control email'})
        self.fields['password'].widget.attrs.update({'class': 'form-control password'})
    def login(self, *args, **kwargs):
        # Add your own processing here.

        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)