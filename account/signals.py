# account/signals.py
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage

User = get_user_model()


@receiver(pre_save, sender=User)
def delete_old_files_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_user = User.objects.get(pk=instance.pk)
    except User.DoesNotExist:
        return

    if old_user.profile_image and old_user.profile_image.name != getattr(instance.profile_image, 'name', None):
        if default_storage.exists(old_user.profile_image.name):
            default_storage.delete(old_user.profile_image.name)

    if old_user.resume_file and old_user.resume_file.name != getattr(instance.resume_file, 'name', None):
        if default_storage.exists(old_user.resume_file.name):
            default_storage.delete(old_user.resume_file.name)


@receiver(post_delete, sender=User)
def delete_files_on_user_delete(sender, instance, **kwargs):
    if instance.profile_image and instance.profile_image.name:
        if default_storage.exists(instance.profile_image.name):
            default_storage.delete(instance.profile_image.name)

    if instance.resume_file and instance.resume_file.name:
        if default_storage.exists(instance.resume_file.name):
            default_storage.delete(instance.resume_file.name)


@receiver(pre_save, sender=User)
def handle_clear_requests(sender, instance, **kwargs):
    if getattr(instance, '_clear_profile_image', False):
        if instance.profile_image and instance.profile_image.name:
            if default_storage.exists(instance.profile_image.name):
                default_storage.delete(instance.profile_image.name)
        instance.profile_image = None

    if getattr(instance, '_clear_resume_file', False):
        if instance.resume_file and instance.resume_file.name:
            if default_storage.exists(instance.resume_file.name):
                default_storage.delete(instance.resume_file.name)
        instance.resume_file = None
