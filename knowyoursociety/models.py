from django.db import models
from .models import *


# Create your models here.

class Committee(models.Model):

    name = models.CharField(max_length=60)
    responsibility = models.CharField(max_length=30)
    appointed_from = models.DateField()
    appointed_till = models.DateField()

    # positions = (
    #     ('PRESIDENT',"PRESIDENT"),
    #     ('VICE_PRESIDENT',"VICE_PRESIDENT"),
    #     ('MEMBER',"MEMBER"),
    # )
    # responsibility = models.CharField(max_length=30,choices=positions,default="MEMBER")

    

    def __str__(self):
        return self.name


class Expense(models.Model):
    type = models.CharField(max_length=500)
    expense = models.IntegerField()

    def __str__(self):
        return self.type