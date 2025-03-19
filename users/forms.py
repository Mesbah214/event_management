from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from events.forms import StyledFormMixin


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class customRegistrationForm(StyledFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'confirm_password']

    def clean_email(self):  # Field error
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already in use')

        return email

    def clean_password(self):  # Field error
        symbols = ['$', '@', '#', '%']
        password = self.cleaned_data.get('password')
        errors = []

        if len(password) < 8:
            errors.append(
                'Password must be at least 8 characters long')

        if not any(char.isdigit() for char in password):
            errors.append(
                'Password must contain at least one digit')

        if not any(char.isupper() for char in password):
            errors.append(
                'Password must contain at least one uppercase letter')

        if not any(char.islower() for char in password):
            errors.append(
                'Password must contain at least one lowercase letter')

        if not any(char in symbols for char in password):
            errors.append(
                'Password must contain at least one of the following symbols: $, @, #, %')

        if errors:
            raise forms.ValidationError(errors)

        return password

    def save(self, commit=True):
        user = super(customRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        return user

    def clean(self):  # Non field error
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
                raise forms.ValidationError('Passwords do not match')

        return cleaned_data
