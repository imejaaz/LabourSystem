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
    cnic = models.CharField(max_length=13, unique=True, verbose_name="CNIC")
    phone = models.CharField(max_length=11, unique=True, verbose_name="Phone Number")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Gender")
    address = models.TextField(verbose_name="Address")
    skill = models.TextField(verbose_name="Skill Set")
    work_experience = models.TextField(verbose_name="Work Experience", blank=True, null=True)
    application_id = models.CharField(max_length=10, unique=True, editable=False, verbose_name="application id")
    def save(self, *args, **kwargs):
        if not self.application_id:
            self.application_id = self.generate_application_id()
        super(Applicant, self).save(*args, **kwargs)

    def generate_application_id(self):
        prefix = 'apid'
        last_application = Applicant.objects.filter(application_id__startswith=prefix).order_by(
           '-application_id').first()
        if last_application:
            last_id = int(last_application.application_id[len(prefix):])
            new_id = f"{prefix}{last_id + 1:03d}"
        else:
            new_id = f"{prefix}0001"
        return new_id

    def __str__(self):
        return self.application_id




class InterViewResults(models.Model):
    applicant = models.OneToOneField(Applicant, on_delete=models.CASCADE, related_name='scores')
    score = models.FloatField()
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return self.applicant.name
