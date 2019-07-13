from django.conf import settings
from django.apps import AppConfig

from heroku import methods

import logging

LOGGER = logging.getLogger('heroku.apps')


class HerokuConfig(AppConfig):
    name = 'heroku'

    def ready(self):
        LOGGER.info('[Startup] Checking for existing webhooks')
        res = methods.updates.get_webhook_info.get()
        if res['ok']:
            if res['result']['url'] == settings.FULL_UPDATE_URL:
                LOGGER.info(f'[Startup] Found existing webhook for valid url: {res["result"]["url"]}')
                return
            elif res['result']['url'] == '':
                LOGGER.info('[Startup] No webhook found')
            else:
                LOGGER.info(f'[Startup] Found existing webhook for invalid url: {res["result"]["url"]}')
                LOGGER.info('[Startup] Deleting previous webhooks')
                res = methods.updates.delete_webhook.post()
                if res['ok']:
                    LOGGER.info('[Startup] Successfully deleted previous webhooks')
                else:
                    LOGGER.warning(f'[Startup] Failed to delete webhooks:\n{res}')
        else:
            LOGGER.error('[Startup] Error getting webhook info, will attempt to set up webhook')

        LOGGER.info('[Startup] Setting up new webhook')
        res = methods.updates.set_webhook.post({'url': settings.FULL_UPDATE_URL})
        if res['ok']:
            LOGGER.info('[Startup] Successfully set up new webhook')
        else:
            LOGGER.error(f'[Startup] Failed to set up new webhook:\n{res}')
