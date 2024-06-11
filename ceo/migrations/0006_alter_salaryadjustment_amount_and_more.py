# Generated by Django 5.0.6 on 2024-06-11 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceo', '0005_salaryadjustment_for_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaryadjustment',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='salaryadjustment',
            name='percentage',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='salaryadjustment',
            name='reason',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='salaryadjustment',
            name='type',
            field=models.CharField(choices=[('bonus', 'Bonus'), ('deduction', 'Deduction')], default=None, max_length=10),
        ),
    ]