from django.db import models
from account.models import CustomUser


class DegreeChoices(models.TextChoices):
    BACHELOR = 'bachelor', 'Bakalavr'
    MASTER = 'master', 'Magistr'
    PHD = 'phd', 'PhD'
    PROFESSIONAL_COURSE = 'professional_course', 'Kasbiy kurs'


class Education(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='educations')
    university = models.CharField(max_length=150)
    specialization = models.CharField(max_length=150)
    degree = models.CharField(
        max_length=30,
        choices=DegreeChoices.choices,
        default=DegreeChoices.BACHELOR,
        verbose_name="Daraja"
    )
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'education'

    def __str__(self):
        return f"{self.university} - {self.specialization}"
