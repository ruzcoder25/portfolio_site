from django.db import models
from account.models import CustomUser


class LevelChoices(models.TextChoices):
    BEGINNER = 'beginner', 'Beginner'
    ELEMENTARY = 'elementary', 'Elementary'
    PRE_INTERMEDIATE = 'pre-intermediate', 'Pre-Intermediate'
    INTERMEDIATE = 'intermediate', 'Intermediate'
    ADVANCED = 'advanced', 'Advanced'
    NATIVE = 'native', 'Native'


class Language(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='languages')
    name = models.CharField(max_length=150)
    level = models.CharField(max_length=20, choices=LevelChoices.choices, default=LevelChoices.BEGINNER)

    class Meta:
        db_table = 'language'

    def __str__(self):
        return f"{self.name} ({self.level})"
