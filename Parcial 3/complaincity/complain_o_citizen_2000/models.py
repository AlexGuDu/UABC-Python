from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class BigComplaint(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(default='empty')
    type_complaint = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now, blank=True)

class MiniComplaint(models.Model):
    body = models.TextField(default='empty')
    date = models.DateTimeField(default=datetime.now, blank=True)
    bigcomplaint = models.ForeignKey(BigComplaint, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
