# Generated by Django 5.0.6 on 2024-05-21 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labor', '0003_alter_attendance_unique_together_and_more'),
        ('supervisor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewercomment',
            name='commentator',
            field=models.ManyToManyField(blank=True, to='labor.labor'),
        ),
    ]