from django.db import models
from django.conf import settings


# Create your models here.

class ModifiedImage(models.Model):

        modified_image = models.ImageField(upload_to=getattr(settings, "MEDIA_ROOT")+'/detector/', null=True, blank=True)
