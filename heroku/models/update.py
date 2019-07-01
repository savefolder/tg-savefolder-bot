from django.db import models
from django.core.exceptions import ValidationError

from heroku.models import Message


class Update(models.Model):
    update_id = models.IntegerField()
    message = models.OneToOneField(Message, on_delete=models.CASCADE, null=True, related_name='update')
    edited_message = models.OneToOneField(Message, on_delete=models.CASCADE, null=True, related_name='update_edit')

    def clean(self):
        if self.message is None and self.edited_message is None:
            raise ValidationError('One of `message` or `edited_message` must be not null')
