# Generated by Django 5.0.6 on 2024-06-11 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labor', '0006_alter_attendance_check_in_alter_attendance_check_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hourlyattendance',
            name='attendance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_hours', to='labor.attendance'),
        ),
    ]
