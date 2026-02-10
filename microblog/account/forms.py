from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Hasło',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Powtórz hasło',
        widget=forms.PasswordInput
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Hasła nie są identyczne.")
        return cd['password2']
    
# Formularz do modelu Profile
User = get_user_model()

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'date_of_birth', 'photo')
        labels = {
            'bio': 'Opis',
            'date_of_birth': 'Data urodzenia',
            'photo': 'Zdjęcie profilowe',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }