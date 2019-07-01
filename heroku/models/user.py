from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    is_bot = models.BooleanField()
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, blank=True)
    username = models.CharField(max_length=64, blank=True)
