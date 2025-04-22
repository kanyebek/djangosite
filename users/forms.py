from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    confirm_password = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)