from account.models import User
from django.db import models

class Applicant(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]


    user = models.ForeignKey(User, on_delete = models.CASCADE,  related_name = 'applicant')
    name = models.CharField(max_length=100, verbose_name="Name")
    appId = models.CharField(auto)
    cnic = models.CharField(max_length=13, unique=True, verbose_name="CNIC")
    phone = models.CharField(max_length=11, unique=True, verbose_name="Phone Number")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Gender")
    address = models.TextField(verbose_name="Address")
    skill = models.TextField(verbose_name="Skill Set")
    work_experience = models.TextField(verbose_name="Work Experience")

    def __str__(self):
        return self.name




class InterViewResults(models.Model):
    name = models.OneToOneField(Applicant, on_delete=models.CASCADE, related_name='scores')
    score = models.FloatField()
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return self.name.name
