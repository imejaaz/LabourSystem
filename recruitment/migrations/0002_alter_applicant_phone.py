# Generated by Django 5.0.6 on 2024-06-26 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='phone',
            field=models.CharField(max_length=13, unique=True, verbose_name='Phone Number'),
        ),
    ]