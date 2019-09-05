from django.db import models
from django.conf import settings

# Create your models here.

class TestModel(models.Model):
    text = models.CharField(max_length=10)


class UserImage(models.Model):
    image = models.ImageField(upload_to=getattr(settings, "MEDIA_ROOT"), null=True, blank=True,)

