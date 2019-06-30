import requests

from django.conf import settings


class TelegramAPIMethod:
    def __init__(self, method):
        self.method_url = f'{settings.BOT_URL}/{method}'

    def get(self, params_dict=None):
        response = requests.get(self.method_url, params_dict)
        return response.json()

    def post(self, params_dict=None):
        response = requests.post(self.method_url, params_dict)
        return response.json()
