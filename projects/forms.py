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
        ]
        widgets = {
            'project_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Loyiha nomini kiriting'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Loyiha haqida batafsil ma\'lumot',
                'rows': 4
            }),
            'github_link_project': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://github.com/username/project'
            }),
            'live_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://your-project.com'
            }),
            'skill': forms.SelectMultiple(attrs={
                'class': 'form-control skill-select',
                'style': 'height: 150px;'
            }),
            'project_type': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'work_type': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
        }
        labels = {
            'project_name': 'Loyiha Nomi',
            'description': 'Loyiha Tavsifi',
            'github_link_project': 'GitHub Linki',
            'live_link': 'Jonli Demo Linki',
            'skill': 'Ko\'nikmalar',
            'project_type': 'Loyiha Turi',
            'work_type': 'Ish Turi',
        }
        help_texts = {
            'github_link_project': 'Loyihaning GitHub repository manzili (ixtiyoriy)',
            'live_link': 'Loyihaning ishlayotgan demo sayti manzili (ixtiyoriy)',
            'skill': 'Loyihada ishlatilgan texnologiyalar va ko\'nikmalar',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Agar user berilgan bo'lsa, faqat shu userning skill larini ko'rsatish
        if user:
            self.fields['skill'].queryset = Skill.objects.filter(user=user)

        # Majburiy maydonlar
        self.fields['project_name'].required = True
        self.fields['description'].required = True
        self.fields['project_type'].required = True
        self.fields['work_type'].required = True

        # Ko'nikmalar va linklar majburiy emas
        self.fields['skill'].required = False
        self.fields['github_link_project'].required = False
        self.fields['live_link'].required = False

    def clean_project_name(self):
        project_name = self.cleaned_data.get('project_name')
        if len(project_name) < 3:
            raise forms.ValidationError("Loyiha nomi kamida 3 ta belgidan iborat bo'lishi kerak.")
        return project_name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError("Loyiha tavsifi kamida 10 ta belgidan iborat bo'lishi kerak.")
        return description