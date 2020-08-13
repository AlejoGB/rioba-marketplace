from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    adress_1 = models.CharField(max_length=200)
    adress_2 = models.CharField(max_length=200)
    adress_3 = models.CharField(max_length=200)
    adress_4 = models.CharField(max_length=200)
    adress_5 = models.CharField(max_length=200)
    pass