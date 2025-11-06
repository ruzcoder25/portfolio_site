from django.db import models
from django.utils import timezone


class Skill(models.Model):
    """
    Skill modeli — foydalanuvchining ko‘nikmalari (masalan: Python, Django, PostgreSQL) uchun.
    Har bir ko‘nikma ma'lum bir toifaga (category) tegishli.
    """

    CATEGORY_CHOICES = [
        ('programming', 'Dasturlash tillari'),
        ('database', "Ma'lumotlar bazasi"),
        ('framework', 'Framework va kutubxonalar'),
        ('devops', 'DevOps vositalari'),
        ('other', 'Boshqa'),
    ]

    name = models.CharField(
        max_length=100,
        help_text="Ko‘nikma nomi (masalan: Python, Django, Git, Docker)."
    )
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        help_text="Ko‘nikma tegishli bo‘lgan toifa."
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        help_text="Ko‘nikma yaratilgan sana va vaqt."
    )

    class Meta:
        db_table = 'skill'
        ordering = ['category', 'name']
        verbose_name = "Ko‘nikma"
        verbose_name_plural = "Ko‘nikmalar"

    def __str__(self):
        return f"{self.get_category_display()} → {self.name}"
