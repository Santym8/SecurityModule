from django.db import models

# Create your models here.
class Module(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'sec_module'
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'