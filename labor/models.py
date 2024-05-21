from django.db import models
from account.models import User

class Labor(models.Model):
    POST_CHOICES = [
        ('labor', 'Labor'),
        ('supervisor', 'Supervisor'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='labors')
    labor_id = models.CharField(max_length=10, unique=True, editable=False, verbose_name="Labor ID")
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    cnic = models.CharField(max_length=13, unique=True, verbose_name="CNIC")
    phone = models.CharField(max_length=11, unique=True, verbose_name="Phone Number")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Gender")
    address = models.TextField(verbose_name="Address")
    post = models.CharField(max_length=10, choices=POST_CHOICES, verbose_name="Post")
    basic_pay = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Basic Pay")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    date_of_hire = models.DateField(verbose_name="Date of Hire")

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
