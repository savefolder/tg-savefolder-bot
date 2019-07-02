import requests

from django.conf import settings
from django_cron import CronJobBase, Schedule

import logging


LOGGER = logging.getLogger('cron.ping')


class PingCronJob(CronJobBase):
    RUN_EVERY_MINS = 10

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.ping'

    def do(self):
        response = requests.get(f'{settings.SELF_URL}/ping/')
        if response.status_code != 200:
            LOGGER.error('[Ping] Failed to ping self')
