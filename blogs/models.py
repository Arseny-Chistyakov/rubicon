from datetime import date

from django.db import models


class New(models.Model):
    header = models.CharField(max_length=256)
    image = models.ImageField(upload_to='blogs_images')
    body = models.CharField(max_length=256)
    date_public = models.DateField(auto_now=True)

    def __str__(self):
        return self.header
