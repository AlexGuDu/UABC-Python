from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class BigComplaint(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(default='empty')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class MiniComplaint(models.Model):
    body = models.TextField(default='empty')
    bigcomplaint = models.ForeignKey(BigComplaint, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
