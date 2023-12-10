from django.db import models
from AdministrationSite.module.models import Module
# Create your models here.
class Function(models.Model):
    name = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=True)
    
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'sec_function'
        verbose_name = 'Function'
        verbose_name_plural = 'Functions'