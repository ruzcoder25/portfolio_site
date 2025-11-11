from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'full_name',
            'email',
            'phone_number',
            'specialization',
            'profile_image',
            'location',
            'github_link',
            'linkedin_link',
            'resume_file',
            'telegram',
        ]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'full_name',
            'email',
            'phone_number',
            'specialization',
            'profile_image',
            'location',
            'github_link',
            'linkedin_link',
            'resume_file',
            'telegram',
        ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

