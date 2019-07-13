from django.db import models

from heroku.models import TextEntity


class Text(models.Model):
    text = models.CharField(max_length=4096, blank=True)
    entities = models.ManyToManyField(TextEntity)
