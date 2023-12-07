from django.db import models
from AdministrationSite.user.models import User
from AdministrationSite.function.models import Function
# Create your models here.
class Audit(models.Model):
    action = models.CharField(max_length=50)
    description = models.TextField
    observation = models.TextField
    ip = models.CharField(max_length=16)

    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    function_id = models.ForeignKey(Function, on_delete=models.CASCADE)
