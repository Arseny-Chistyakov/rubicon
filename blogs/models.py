from uuid import uuid4

from django.db import models
from django.urls import reverse
from django.utils import timezone

from users.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    uid = models.UUIDField(primary_key=True, default=uuid4, verbose_name='ID')
    title = models.CharField(max_length=256, verbose_name='Заголовок поста')
    image = models.ImageField(upload_to='blogs_post_images', verbose_name='Изображение поста')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста')
    slug = models.SlugField(max_length=250, unique_for_date='publish', unique=True,
                            db_index=True, blank=True, verbose_name='URL')
    body = models.TextField(verbose_name='Содержимое поста')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Время публикации поста')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания поста')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время изменения поста')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='Статус поста')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:post_detail', args=[self.slug])


class Comment(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4, verbose_name='ID')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Никнейм комментатора')
    body = models.TextField(verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Комментарий создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Комментарий изменен')
    active = models.BooleanField(default=True, verbose_name='Статус комментария')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '{} прокомментировал {}'.format(self.user, self.post)
