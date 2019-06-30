import requests

from django.conf import settings


class TelegramAPIMethod:
    def __init__(self, method):
        self.method_url = f'{settings.BOT_URL}/{method}'

    def get(self, **kwargs):
        response = requests.get(self.method_url, **kwargs)
        return response.json()

    def post(self, **kwargs):
        response = requests.post(self.method_url, **kwargs)
        return response.json()
