# Generated by Django 5.0.6 on 2024-06-08 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labor', '0002_attendance_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='created_at',
        ),
    ]