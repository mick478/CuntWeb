# Generated by Django 2.0.7 on 2020-08-18 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200818_0443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motor_part',
            name='part_element1',
        ),
        migrations.AddField(
            model_name='motor_part',
            name='part_element',
            field=models.ManyToManyField(to='home.motor_element'),
        ),
        migrations.AlterField(
            model_name='motor_plate',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.motor_type'),
        ),
        migrations.RemoveField(
            model_name='motor_type',
            name='type_model',
        ),
        migrations.AddField(
            model_name='motor_type',
            name='type_model',
            field=models.ManyToManyField(to='home.motor_part'),
        ),
    ]
