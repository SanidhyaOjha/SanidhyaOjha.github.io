from django.db import models
import datetime
# Create your models here.
class Blog(models.Model):
    title =models.CharField(100)
    content = models.TextField(default=None)
    author = models.CharField(100)
    timestamp = models.DateTimeField(default=None)