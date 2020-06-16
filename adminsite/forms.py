from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': "shadow appearance-none w-full bg-white border border-grey-light hover:border-grey px-2 py-2 rounded shadow",
         'placeholder':"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class":"shadow appearance-none w-full bg-white border border-grey-light hover:border-grey px-2 py-2 rounded shadow" ,
            'placeholder':"Your Password"
        }
))