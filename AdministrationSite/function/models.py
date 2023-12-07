from django.db import models
from AdministrationSite.module.models import Module
# Create your models here.
class Function(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE)