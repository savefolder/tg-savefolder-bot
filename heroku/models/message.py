from django.db import models

from heroku.models import User, Chat


class Message(models.Model):
    message_id = models.IntegerField()
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='messages')
    date = models.DateTimeField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    text = models.CharField(max_length=4096, blank=True)
