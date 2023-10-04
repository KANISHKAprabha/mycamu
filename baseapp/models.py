from django.db import models
from django.contrib.auth.models import User



class Home(models.Model):
    user_role=[
        ('Student','Student'),
        ('Teacher','Teacher'),
        ('Admin','Admin'),
    ]
    options=models.CharField(max_length=10,choices=user_role,null=False,default='Admin')

# Create your models here.
