from django.conf import settings
from django.apps import AppConfig

from heroku import methods

import logging

LOGGER = logging.getLogger('heroku.apps')


class HerokuConfig(AppConfig):
    name = 'heroku'

    def ready(self):
        LOGGER.info('[Startup] Deleting previous webhooks')
        res = methods.delete_webhook.post()
        if res['code'] != 200:
            LOGGER.warning(f'[Startup] Failed to delete webhooks:\n{res}')
        else:
            LOGGER.info('[Startup] Successfully deleted previous webhooks')

        LOGGER.info('[Startup] Setting up new webhook')
        res = methods.set_webhook.post({'url': settings.SELF_URL})
        if res['code'] != 200:
            LOGGER.error(f'[Startup] Failed to set up new webhook:\n{res}')
        else:
            LOGGER.info('[Startup] Successfully set up new webhook')
