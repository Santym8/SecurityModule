from django.db import models
from AdministrationSite.user.models import User
from AdministrationSite.function.models import Function
# Create your models here.
class Audit(models.Model):
    action = models.CharField(max_length=50)
    description = models.TextField()
    observation = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=16)
    date = models.DateTimeField()

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    function_id = models.ForeignKey(Function, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.action
    
    class Meta:
        db_table = 'sec_audit'
        verbose_name = 'Audit'
        verbose_name_plural = 'Audits'

    

    
