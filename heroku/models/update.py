from django.db import models

from utils import CustomManager
from heroku.models import Message


class Update(models.Model):
    objects = CustomManager()

    update_id = models.IntegerField()
    message = models.OneToOneField(Message, on_delete=models.CASCADE, null=True, blank=True, related_name='update')
