from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ("user", "User"),
        ("ceo", "CEO"),
        ("labour", "Labour"),
        ("supervisor", "Supervisor"),
    ]
    role = models.CharField(max_length=25, choices=ROLE_CHOICES, default="user")
    basic_salary = models.IntegerField(default=0)
    cnic = models.CharField(max_length=13, null=True, blank=True)
    

