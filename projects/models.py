# project/models.py
from django.db import models
from account.models import CustomUser
from skill.models import Skill
from django.utils import timezone


class Project(models.Model):
    PROJECT_TYPE_CHOICES = [
        ('real', 'Real loyiha'),
        ('practice', 'Tajriba loyihasi'),
    ]

    WORK_TYPE_CHOICES = [
        ('team', 'Jamoaviy ish'),
        ('active', 'Hozirgi ish'),
        ('learning', 'O\'rganish uchun'),
        ('personal', 'Shaxsiy loyiha'),
    ]

    project_name = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='projects')
    github_link_project = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    skill = models.ManyToManyField(Skill, related_name='projects', blank=True)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOICES, default='practice')
    work_type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES, default='personal')
    created_at = models.DateTimeField(default=timezone.now)


    class Meta:
        db_table = 'project'
        ordering = ['-created_at']

    def __str__(self):
        return self.project_name