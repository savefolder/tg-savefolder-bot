from django.db import models

from heroku.models import Message


class Update(models.Model):
    update_id = models.IntegerField()
    message = models.OneToOneField(Message, on_delete=models.CASCADE, null=True, related_name='update')
