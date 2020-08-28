# Generated by Django 2.0.7 on 2020-08-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200818_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='fix_history',
            name='element_name',
            field=models.CharField(default=321, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='motor_plate',
            name='history',
            field=models.ManyToManyField(blank=True, null=True, to='home.fix_history'),
        ),
        migrations.AlterField(
            model_name='motor_element',
            name='element_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='motor_part',
            name='part_element',
            field=models.ManyToManyField(related_name='motor_element_element_name', to='home.motor_element'),
        ),
    ]
