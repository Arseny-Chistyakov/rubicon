from django.db import models
from django.urls import reverse
from django.utils import timezone

from users.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    header = models.CharField(max_length=256)
    image = models.ImageField(upload_to='blogs_post_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique_for_date='publish', unique=True, verbose_name='URL',
                            db_index=True, blank=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('blogs:post_detail', args=[self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
