from datetime import timedelta
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


class User(AbstractUser):
    uid = models.UUIDField(primary_key=True, default=uuid4, verbose_name='ID')
    age = models.PositiveIntegerField(default=18, verbose_name='Возраст')
    email = models.EmailField(unique=True, verbose_name='Почта')
    image = models.ImageField(upload_to='users_images', null=True, blank=True, verbose_name='Фотография')
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(auto_now=True, blank=True)

    def safe_delete_user(self):
        self.is_active = False
        self.save()

    def is_activation_key_expires(self):
        if now() <= self.activation_key_expires + timedelta(hours=48):
            return False
        return True


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )
    user = models.OneToOneField(User, unique=True, db_index=True, on_delete=models.CASCADE, primary_key=True,
                                verbose_name='Профиль пользователя')
    about = models.TextField(blank=True, null=False, verbose_name='О себе')
    gender = models.CharField(choices=GENDER_CHOICES, blank=True, max_length=2, verbose_name='Пол')
    langs = models.CharField(blank=True, max_length=100, default='RU', verbose_name='Язык')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        if not created:
            instance.userprofile.save()
