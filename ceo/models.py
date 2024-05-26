from django.db import models

from django.db import models
from django.utils import timezone
from labor.models import User, Labor

class SalaryAdjustment(models.Model):
    SALARY_ADJUSTMENT_TYPES = [
        ('bonus', 'Bonus'),
        ('deduction', 'Deduction'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    reason = models.TextField()
    type = models.CharField(max_length=10, choices=SALARY_ADJUSTMENT_TYPES)
    added_by = models.ForeignKey(Labor, on_delete=models.SET_NULL, null=True, blank=True, related_name='salary_adjustment')

    def __str__(self):
        if self.amount is not None:
            return f"{self.get_type_display()} of {self.amount} on {self.date} added by {self.added_by}"
        elif self.percentage is not None:
            return f"{self.get_type_display()} of {self.percentage}% on {self.date} added by {self.added_by}"

class SalaryRecord(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    ]

    labor = models.ForeignKey(Labor, on_delete=models.CASCADE, related_name='salary_records')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.CharField(max_length=20)  # e.g., "January 2023"
    days_worked = models.IntegerField()  # Number of days worked in the month
    extra_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Extra hours worked
    adjustment = models.ForeignKey(SalaryAdjustment, on_delete=models.SET_NULL, null=True, blank=True, related_name='salary_records')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.labor} - {self.amount} for {self.month} (Days worked: {self.days_worked}, Extra hours: {self.extra_hours}, Status: {self.get_status_display()})"


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    progress_report = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Percentage value between 0.00 and 100.00
    members = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name