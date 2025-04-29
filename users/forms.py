from django import forms

class RegisterForm(forms.Form):
    avatar = forms.ImageField()
    age = forms.IntegerField()
    username = forms.CharField()
    password = forms.CharField()
    confirm_password = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)