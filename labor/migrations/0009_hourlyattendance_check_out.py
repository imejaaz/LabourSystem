# Generated by Django 5.0.6 on 2024-06-11 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labor', '0008_hourlyattendance_hours_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hourlyattendance',
            name='check_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
