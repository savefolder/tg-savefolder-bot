import enum
from django.db import models

from heroku.models import User


class TextEntity(models.Model):
    @enum.unique
    class Type(enum.Enum):
        mention = 'mention'
        hashtag = 'hashtag'
        cashtag = 'cashtag'
        bot_command = 'bot_command'
        url = 'url'
        email = 'email'
        phone_number = 'phone_number'
        bold = 'bold'
        italic = 'italic'
        code = 'code'
        pre = 'pre'
        text_link = 'text_link'
        text_mention = 'text_mention'

    type = models.CharField(
        max_length=16,
        choices=(
            (Type.mention.value,) * 2,
            (Type.hashtag.value,) * 2,
            (Type.cashtag.value,) * 2,
            (Type.bot_command.value,) * 2,
            (Type.url.value,) * 2,
            (Type.email.value,) * 2,
            (Type.phone_number.value,) * 2,
            (Type.bold.value,) * 2,
            (Type.italic.value,) * 2,
            (Type.code.value,) * 2,
            (Type.pre.value,) * 2,
            (Type.text_link.value,) * 2,
            (Type.text_mention.value,) * 2,
        ),
    )
    offset = models.IntegerField()
    length = models.IntegerField()
    url = models.CharField(max_length=256, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
