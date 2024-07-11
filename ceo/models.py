from django.db import models

from django.db import models
from django.utils import timezone
from labor.models import User, Labor

class SalaryAdjustment(models.Model):
    SALARY_ADJUSTMENT_TYPES = [
        ('bonus', 'Bonus'),
        ('deduction', 'Deduction'),
    ]

    amount = models.DecimalField(default=None, max_digits=10, decimal_places=2, null=True, blank=True)
    percentage = models.DecimalField(default=None, max_digits=5, decimal_places=2, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    for_month = models.IntegerField(default=0)
    reason = models.TextField(default=None)
    type = models.CharField(default=None, max_length=10, choices=SALARY_ADJUSTMENT_TYPES)
    added_by = models.ForeignKey(Labor, on_delete=models.SET_NULL, null=True, blank=True, related_name='salary_adjustment')

    def __str__(self):
        if self.amount is not None:
            return f"{self.get_type_display()} of {self.amount} "
        elif self.percentage is not None:
            return f"{self.get_type_display()} of {self.percentage}%"

class Salary(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    ]

    labor = models.ForeignKey(Labor, on_delete=models.CASCADE, related_name='salary_records')
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()
    days_worked = models.IntegerField(default=0)
    extra_hours_wages = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    adjustment = models.ForeignKey(SalaryAdjustment, on_delete=models.SET_NULL, null=True, blank=True, related_name='salary_records')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.labor} - {self.gross_salary} for {self.month} (Days worked: {self.days_worked}, Status: {self.get_status_display()})"


class Project(models.Model):
    CURRENT_STATUS = [
        ("pending", "Pending"),
        ("todo", "Todo"),
        ("doing", "Doing"),
        ("testing", "Testing"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
        
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    deadline = models.DateField(null=True, blank=True)
    currentStatus = models.CharField(choices=CURRENT_STATUS, max_length=15, default="pending")
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    supervisor = models.ForeignKey(Labor, blank=True, null=True, on_delete=models.CASCADE)
    members = models.ManyToManyField(Labor, related_name='projects', blank=True, null=True)

    def __str__(self):
        return self.name
    
    
class Departments(models.Model):
    name = models.CharField(max_length=255)
    labor = models.ManyToManyField(Labor, related_name='departments', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class Designations(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title