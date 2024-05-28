from django.db import models
from account.models import User
from datetime import timezone, date
from django.core.exceptions import ValidationError
class Labor(models.Model):
    POST_CHOICES = [
        ('labor', 'Labor'),
        ('supervisor', 'Supervisor'),
        ('ceo', 'CEO'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='labors')
    labor_id = models.CharField(max_length=10, unique=True, editable=False, verbose_name="Labor ID")
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    cnic = models.CharField(max_length=13, unique=True, verbose_name="CNIC")
    phone = models.CharField(max_length=11, unique=True, verbose_name="Phone Number")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Gender")
    address = models.TextField(verbose_name="Address")
    post = models.CharField(max_length=10, choices=POST_CHOICES, verbose_name="Post", default = 'Labor')
    basic_pay = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Basic Pay")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    date_of_hire = models.DateField(verbose_name="Date of Hire", auto_now_add=True)

    def username(self):
        return f'{self.first_name} {self.last_name}'
    def save(self, *args, **kwargs):
        if not self.labor_id:
            self.labor_id = self.generate_labor_id()
        super(Labor, self).save(*args, **kwargs)

    def generate_labor_id(self):
        prefix = 'LAB'
        last_labor = Labor.objects.filter(labor_id__startswith=prefix).order_by('-labor_id').first()
        if last_labor:
            last_id = int(last_labor.labor_id[len(prefix):])
            new_id = f"{prefix}{last_id + 1:04d}"
        else:
            new_id = f"{prefix}0001"
        return new_id

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.labor_id} -  {self.post}"

    class Meta:
        verbose_name = "Labor"
        verbose_name_plural = "Labors"
        ordering = ['first_name', 'last_name']


class Attendance(models.Model):
    ATTENDANCE_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('leave', 'Leave')
    ]

    labor = models.ForeignKey(Labor, on_delete=models.CASCADE, related_name="attendance")
    date = models.DateField(auto_now_add=True)
    check_in = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES)

    def save(self, *args, **kwargs):
        if not self.pk:
            if Attendance.objects.filter(labor=self.labor, date=date.today()).exists():
                raise ValidationError('Attendance for this labor on this date already exists.')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.labor} - {self.date}"
    class Meta:
        unique_together = ('labor', 'date')
        verbose_name_plural = "Attendance"


class HourlyAttendance(models.Model):
    ATTENDANCE_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('leave', 'Leave')
    ]

    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    check_in = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES)

    def __str__(self):
        return f"{self.attendance} - {self.status}"

    class Meta:
        verbose_name_plural = "Hourly Attendance"
        unique_together = ('check_in', 'attendance')
