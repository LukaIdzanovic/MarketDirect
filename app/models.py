

# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models import Q



class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    vendor = models.BooleanField()
    def __str__(self):
        return f"{self.id} - {self.name}"
