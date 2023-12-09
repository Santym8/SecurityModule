from django.db import models
from ..function.models import Function
# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=True)

    functions = models.ManyToManyField(Function)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'sec_role'
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'