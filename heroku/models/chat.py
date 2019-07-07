from django.db import models

from utils import CustomManager


class Chat(models.Model):
    objects = CustomManager()

    TYPES = (
        ('private', 'private'),
        ('group', 'group'),
        ('supergroup', 'supergroup'),
        ('channel', 'channel'),
    )

    id = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=16, choices=TYPES)
