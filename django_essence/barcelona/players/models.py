from django.db import models

# Create your models here.
class Players(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    dob = models.DateField(null=True)