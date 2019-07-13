import enum
from django.db import models

from utils import CustomManager


class Chat(models.Model):
    objects = CustomManager()

    @enum.unique
    class Type(enum.Enum):
        private = 'private'
        group = 'group'
        supergroup = 'supergroup'
        channel = 'channel'

    id = models.BigIntegerField(primary_key=True)
    type = models.CharField(
        max_length=16,
        choices=(
            (Type.private.value,) * 2,
            (Type.group.value,) * 2,
            (Type.supergroup.value,) * 2,
            (Type.channel.value,) * 2,
        ),
    )
