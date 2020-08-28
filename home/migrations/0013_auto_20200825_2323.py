# Generated by Django 2.0.7 on 2020-08-25 13:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0012_auto_20200825_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motor_plate',
            name='user',
        ),
        migrations.AddField(
            model_name='motor_plate',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
