from django.db import models


class NewAdmin(models.Model):
    header = models.CharField(max_length=256)
    image = models.ImageField(upload_to='blogs_images')
    body = models.TextField()

    def __str__(self):
        return self.header
