# Generated by Django 5.0.6 on 2024-06-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labor', '0010_alter_hourlyattendance_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hourlyattendance',
            name='status',
        ),
        migrations.AlterField(
            model_name='hourlyattendance',
            name='hours',
            field=models.IntegerField(default=0),
        ),
    ]
