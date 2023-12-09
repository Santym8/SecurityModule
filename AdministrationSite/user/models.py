from django.db import models
from ..role.models import Role

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=16,primary_key=True)
    email = models.EmailField()
    dni = models.CharField(max_length=20)
    password = models.CharField(max_length=16)
    status = models.BooleanField(default=True)

    roles = models.ManyToManyField(Role)


    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'sec_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
