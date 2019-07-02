from django.db import models


class Photo(models.Model):
    file_id = models.CharField(max_length=256)
    width = models.IntegerField()
    height = models.IntegerField()
    file_size = models.IntegerField(null=True)
