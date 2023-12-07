from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=16,primary_key=True)
    email = models.EmailField()
    dni = models.CharField(max_length=20)
    password = models.CharField(max_length=16)
    status = models.BooleanField(default=True)
