# Generated by Django 5.0.6 on 2024-05-22 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceo', '0001_initial'),
        ('labor', '0003_alter_attendance_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaryadjustment',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salary_adjustment', to='labor.labor'),
        ),
    ]
