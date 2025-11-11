# account/signals.py
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage
import os

User = get_user_model()


@receiver(pre_save, sender=User)
def delete_old_files_on_update(sender, instance, **kwargs):
    """
    User model yangilanganda eski fayllarni o'chirish
    """
    # Agar yangi user bo'lsa (create), hech narsa qilma
    if not instance.pk:
        return

    try:
        # Eski user ma'lumotlarini olish
        old_user = User.objects.get(pk=instance.pk)
    except User.DoesNotExist:
        return

    # Profil rasmini tekshirish
    if hasattr(old_user, 'profile_image') and old_user.profile_image:
        if hasattr(instance, 'profile_image') and old_user.profile_image != instance.profile_image:
            # Eski rasm faylini o'chirish
            if old_user.profile_image.name:
                try:
                    if default_storage.exists(old_user.profile_image.name):
                        default_storage.delete(old_user.profile_image.name)
                        print(f"✅ Eski profil rasmi o'chirildi: {old_user.profile_image.name}")
                except Exception as e:
                    print(f"❌ Profil rasmini o'chirishda xatolik: {e}")

    # Rezyume faylini tekshirish
    if hasattr(old_user, 'resume_file') and old_user.resume_file:
        if hasattr(instance, 'resume_file') and old_user.resume_file != instance.resume_file:
            # Eski rezyume faylini o'chirish
            if old_user.resume_file.name:
                try:
                    if default_storage.exists(old_user.resume_file.name):
                        default_storage.delete(old_user.resume_file.name)
                        print(f"✅ Eski rezyume fayli o'chirildi: {old_user.resume_file.name}")
                except Exception as e:
                    print(f"❌ Rezyume faylini o'chirishda xatolik: {e}")


@receiver(post_delete, sender=User)
def delete_files_on_user_delete(sender, instance, **kwargs):
    """
    User o'chirilganda uning fayllarini ham o'chirish
    """
    # Profil rasmini o'chirish
    if hasattr(instance, 'profile_image') and instance.profile_image:
        if instance.profile_image.name:
            try:
                if default_storage.exists(instance.profile_image.name):
                    default_storage.delete(instance.profile_image.name)
                    print(f"🗑️ Profil rasmi o'chirildi: {instance.profile_image.name}")
            except Exception as e:
                print(f"❌ Profil rasmini o'chirishda xatolik: {e}")

    # Rezyume faylini o'chirish
    if hasattr(instance, 'resume_file') and instance.resume_file:
        if instance.resume_file.name:
            try:
                if default_storage.exists(instance.resume_file.name):
                    default_storage.delete(instance.resume_file.name)
                    print(f"🗑️ Rezyume fayli o'chirildi: {instance.resume_file.name}")
            except Exception as e:
                print(f"❌ Rezyume faylini o'chirishda xatolik: {e}")


@receiver(pre_save, sender=User)
def handle_clear_requests(sender, instance, **kwargs):
    """
    Clear so'rovlarini qayta ishlash
    """
    # Clear profile image so'rovi
    if hasattr(instance, '_clear_profile_image') and instance._clear_profile_image:
        if hasattr(instance, 'profile_image') and instance.profile_image:
            if instance.profile_image.name:
                try:
                    if default_storage.exists(instance.profile_image.name):
                        default_storage.delete(instance.profile_image.name)
                        print(f"🧹 Profil rasmi clear orqali o'chirildi: {instance.profile_image.name}")
                except Exception as e:
                    print(f"❌ Profil rasmini clear qilishda xatolik: {e}")
            # Field ni None qilish
            instance.profile_image = None

    # Clear resume file so'rovi
    if hasattr(instance, '_clear_resume_file') and instance._clear_resume_file:
        if hasattr(instance, 'resume_file') and instance.resume_file:
            if instance.resume_file.name:
                try:
                    if default_storage.exists(instance.resume_file.name):
                        default_storage.delete(instance.resume_file.name)
                        print(f"🧹 Rezyume fayli clear orqali o'chirildi: {instance.resume_file.name}")
                except Exception as e:
                    print(f"❌ Rezyume faylini clear qilishda xatolik: {e}")
            # Field ni None qilish
            instance.resume_file = None