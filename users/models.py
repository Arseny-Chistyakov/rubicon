from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(auto_now=True, blank=True)

    def safe_delete_user(self):
        self.is_active = False
        self.save()

    def is_activation_key_expires(self):
        if now() <= self.activation_key_expires + timedelta(hours=48):
            return False
        return True
