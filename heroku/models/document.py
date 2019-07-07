from django.db import models

from utils import CustomManager
from heroku.models import Photo


class Document(models.Model):
    objects = CustomManager()

    file_id = models.CharField(max_length=256)
    thumb = models.OneToOneField(Photo, on_delete=models.CASCADE, null=True, related_name='document')
    file_name = models.CharField(max_length=256, blank=True)
    mime_type = models.CharField(max_length=64, blank=True)
    file_size = models.IntegerField(null=True)
