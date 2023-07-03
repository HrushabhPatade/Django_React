from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()
    message= models.TextField()

# Create your models here.
