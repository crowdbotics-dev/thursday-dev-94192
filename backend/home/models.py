from django.conf import settings
from django.db import models
class Job(models.Model):
    'Generated Model'
    title = models.CharField(max_length=256,)
    user = models.ForeignKey("users.User",on_delete=models.CASCADE,null=True,blank=True,related_name="job_user",)
