from django.db import models

# Create your models here.
class SwPackage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    dept = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'SwPackages'

class Dept(models.Model):
    name = models.CharField(max_length=100)
