from django import forms


class RegisterUserForm(forms.Form):
    login = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    email = forms.EmailField()


class LoginUserForm(forms.Form):
    login = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
