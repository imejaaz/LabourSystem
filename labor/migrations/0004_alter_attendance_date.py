# Generated by Django 5.0.6 on 2024-06-09 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labor', '0003_remove_attendance_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
