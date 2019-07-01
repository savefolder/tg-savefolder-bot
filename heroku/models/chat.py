from django.db import models


class Chat(models.Model):
    CHAT_TYPES = [
        'private',
        'group',
        'supergroup',
        'channel',
    ]

    id = models.BigIntegerField(primary_key=True)
    chat_type = models.CharField(max_length=16, choices=CHAT_TYPES)
