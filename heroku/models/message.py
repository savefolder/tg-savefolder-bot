import enum
from django.db import models

from utils import CustomManager
from heroku.models import User, Chat, Document, Photo, Text


class Message(models.Model):
    objects = CustomManager()

    @enum.unique
    class Type(enum.Enum):
        text = 'text'
        document = 'document'
        photo = 'photo'

    message_id = models.IntegerField()
    type = models.CharField(
        max_length=16,
        choices=(
            (Type.text.value,) * 2,
            (Type.document.value,) * 2,
            (Type.photo.value,) * 2,
        ),
    )
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='messages')
    date = models.DateTimeField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    text = models.OneToOneField(Text, on_delete=models.CASCADE, null=True, blank=True)
    document = models.OneToOneField(Document, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.OneToOneField(Photo, on_delete=models.CASCADE, null=True, blank=True)
