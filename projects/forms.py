from django import forms
from .models import Project
from skill.models import Skill

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'project_name',
            'description',
            'github_link_project',
            'live_link',
            'skill',
            'project_type',
            'work_type',
            'order',
        ]
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Loyiha nomi'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Loyiha haqida batafsil', 'rows': 4}),
            'github_link_project': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'GitHub link'}),
            'live_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Loyihaning jonli linki'}),
            'skill': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'project_type': forms.Select(attrs={'class': 'form-control'}),
            'work_type': forms.Select(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

