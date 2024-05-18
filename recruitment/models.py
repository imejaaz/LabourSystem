from django.db import models
from account.models import User

class InterViewResults(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    InterViewScore = models.FloatField()
    is_selected = models.BooleanField(default=False)
    position = models.CharField(max_length=25, default="None")

    def __str__(self):
        return f'{self.user}  position: {self.position}'
    