from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=True)