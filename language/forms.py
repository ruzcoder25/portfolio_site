from django import forms

from .models import Language


class LanguageForm(forms.Form):
    class Meta:
        model = Language
        fields = [
            'name',
            'level'
        ]