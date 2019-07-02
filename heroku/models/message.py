from django.db import models
from django.contrib.postgres import fields

from heroku.models import User, Chat, Document, Photo


class Message(models.Model):
    TYPES = (
        ('text', 'text'),
        ('document', 'document'),
        ('photo', 'photo'),
    )

    message_id = models.IntegerField()
    type = models.CharField(max_length=16, choices=TYPES)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='messages')
    date = models.DateTimeField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    text = models.CharField(max_length=4096, blank=True)
    document = models.ForeignKey(Document, on_delete=models.SET_NULL, null=True)
    photos = fields.ArrayField(Photo, null=True)
