from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class CustomManager(models.Manager):
    def get_or_none(self, *args, **kwargs):
        try:
            result = self.get(*args, **kwargs)
        except ObjectDoesNotExist:
            result = None
        return result
