# Generated by Django 5.0.6 on 2024-05-28 02:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('submitted', 'Submitted'), ('under_review', 'Under Review'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='submitted', max_length=20)),
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
