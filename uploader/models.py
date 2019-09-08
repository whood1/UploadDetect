from django.db import models
from django.conf import settings

# Create your models here.


class UserImage(models.Model):
    uploader_file_loacation = getattr(settings, "MEDIA_ROOT")+'/uploader/'
    image = models.ImageField(upload_to=uploader_file_loacation, null=True, blank=True,)

