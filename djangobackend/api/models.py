from django.db import models


class Students(models.Model):
    stuname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

# Create your models here.
