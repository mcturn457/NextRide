from django import forms
from django.contrib.auth.models import User


class RegisterFormUser(forms.Form):
    first_name = forms.CharField(max_length=100, label='Vorname')
    last_name = forms.CharField(max_length=100, label='Nachname')
    street = forms.CharField(max_length=100, label='Straße & Hausnummer', required=False)
    postalcode = forms.CharField(max_length=100, label='PLZ', required=False)
    city = forms.CharField(max_length=100, label='Stadt', required=False)

    username = forms.EmailField(max_length=100, label='Email')
    password = forms.CharField(min_length=8, max_length=100, label='Passwort', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Ein Account mit dieser Email ist schon vergeben')
        return username


class RegisterFormCompany(forms.Form):
    name = forms.CharField(max_length=100, label='Firmenname', required=True, empty_value='Test')
    street = forms.CharField(max_length=100, label='Straße & Hausnummer', required=True)
    postalcode = forms.CharField(max_length=100, label='PLZ', required=True)
    city = forms.CharField(max_length=100, label='Stadt', required=True)

    username = forms.EmailField(max_length=100, label='Email')
    password = forms.CharField(min_length=8, max_length=100, label='Passwort', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Ein Account mit dieser Email ist schon vergeben')
        return username


class LoginForm(forms.Form):
    username = forms.EmailField(label='Email')
    password = forms.CharField(label='Passwort', widget=forms.PasswordInput)
