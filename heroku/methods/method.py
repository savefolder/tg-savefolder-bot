import requests

from settings import BOT_URL


class TelegramAPIMethod:
    def __init__(self, method):
        self.method_url = f'{BOT_URL}/{method}'

    def __call__(self, **kwargs):
        response = requests.get(self.method_url, **kwargs)
        return response.json()
