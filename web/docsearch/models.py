from django.db import models

# Create your models here.
class File(models.Model):
    filename = models.CharField(max_length=100, unique=True)
    text = models.TextField()
