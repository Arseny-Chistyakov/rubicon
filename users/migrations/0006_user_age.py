# Generated by Django 3.2.12 on 2022-05-11 12:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0005_auto_20220511_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(default=18),
        ),
    ]
