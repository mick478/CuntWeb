# Generated by Django 2.0.7 on 2020-08-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200824_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='fix_history',
            name='plate',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
