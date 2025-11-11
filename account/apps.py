# account/apps.py
from django.apps import AppConfig

class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

    def ready(self):
        """
        Signalarni import qilish va faollashtirish
        """
        import account.signals