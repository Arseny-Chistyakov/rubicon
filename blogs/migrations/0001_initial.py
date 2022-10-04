# Generated by Django 3.2.12 on 2022-10-04 08:54

import uuid

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок поста')),
                ('image', models.ImageField(upload_to='blogs_post_images', verbose_name='Изображение поста')),
                ('slug', models.SlugField(blank=True, max_length=250, unique=True, unique_for_date='publish',
                                          verbose_name='URL')),
                ('body', models.TextField(verbose_name='Содержимое поста')),
                ('publish',
                 models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время публикации поста')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания поста')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Время изменения поста')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft',
                                            max_length=10, verbose_name='Статус поста')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                             verbose_name='Автор поста')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Комментарий создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Комментарий изменен')),
                ('active', models.BooleanField(default=True, verbose_name='Статус комментария')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments',
                                           to='blogs.post', verbose_name='Пост')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_user',
                                           to=settings.AUTH_USER_MODEL, verbose_name='Никнейм комментатора')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
