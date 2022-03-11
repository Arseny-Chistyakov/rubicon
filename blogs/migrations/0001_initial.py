# Generated by Django 4.0.3 on 2022-03-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='')),
                ('body', models.CharField(max_length=256)),
                ('date_public', models.DateField(auto_now=True)),
            ],
        ),
    ]
