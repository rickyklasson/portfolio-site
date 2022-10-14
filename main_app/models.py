from queue import Empty
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    web_url = models.CharField(max_length=100)

    img = models.ImageField(upload_to='proj_images', blank=True)

    def __str__(self):
        return self.title
