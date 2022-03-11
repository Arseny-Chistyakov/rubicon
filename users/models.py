from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)

    def safe_delete_user(self):
        self.is_active = False
        self.save()
