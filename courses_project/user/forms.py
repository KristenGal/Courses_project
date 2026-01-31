from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser
from captcha.fields import CaptchaField



class RegistrationForm(UserCreationForm):
    captcha = CaptchaField(label="Enter the text from the image")
    class Meta:
        model = CustomUser
        fields = ("full_name", "role", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = True
        user.save()
        return user
    

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("full_name", "role", "email", "phone_number")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].disabled = True
