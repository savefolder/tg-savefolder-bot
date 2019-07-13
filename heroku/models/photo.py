from django.db import models

from utils import CustomManager


class Photo(models.Model):
    objects = CustomManager()

    file_id = models.CharField(max_length=256)
    width = models.IntegerField()
    height = models.IntegerField()
    file_size = models.IntegerField(null=True, blank=True)
