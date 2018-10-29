from django.db import models
from datetime import datetime

# Create your models here.
class Paper(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Papers'


class PaperCategory(models.Model):
    name = models.CharField(max_length=100)
