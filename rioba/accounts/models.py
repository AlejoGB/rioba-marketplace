from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100 , default=0)
    email = models.CharField(max_length=50 , default=0)
    phone = models.CharField(max_length=20 , default=0)
    adress_1 = models.CharField(max_length=200 , default=0)
    adress_2 = models.CharField(max_length=200 , default=0)
    adress_3 = models.CharField(max_length=200 , default=0)
    adress_4 = models.CharField(max_length=200 , default=0)
    adress_5 = models.CharField(max_length=200 , default=0)
    pass