# Generated by Django 5.0.6 on 2024-06-08 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labor', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('app_id', models.CharField(max_length=10, verbose_name='Application ID')),
                ('description', models.TextField()),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('save', 'Saved'), ('submitted', 'Submitted'), ('under_review', 'Under Review'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='save', max_length=20)),
                ('labor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='labor.labor')),
            ],
            options={
                'verbose_name_plural': 'Applications',
            },
        ),
        migrations.CreateModel(
            name='ApplicationDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='application_documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='supervisor.application')),
            ],
            options={
                'verbose_name_plural': 'Application Documents',
            },
        ),
        migrations.CreateModel(
            name='ReviewerComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='supervisor.application')),
                ('commentator', models.ManyToManyField(blank=True, to='labor.labor')),
            ],
            options={
                'verbose_name_plural': 'Reviewer Comments',
            },
        ),
    ]
