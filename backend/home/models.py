from django.conf import settings
from django.db import models
class Job(models.Model):
    'Generated Model'
    user = models.ForeignKey("users.User",null=True,blank=True,on_delete=models.CASCADE,related_name="job_user",)
