from django import forms
from .models import Education

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['university', 'specialization', 'degree', 'start_year', 'end_year']
        widgets = {
            'university': forms.TextInput(attrs={'class': 'form-control'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'start_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'YYYY'}),
            'end_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'YYYY'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_year = cleaned_data.get('start_year')
        end_year = cleaned_data.get('end_year')
        if start_year and end_year and start_year > end_year:
            raise forms.ValidationError("Boshlanish yili tugash yilidan katta bo'lishi mumkin emas ❌")
        return cleaned_data
