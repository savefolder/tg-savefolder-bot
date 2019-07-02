from heroku.methods.method import TelegramAPIMethod


class GetUpdates(TelegramAPIMethod):
    METHOD = 'getUpdates'

    def __init__(self):
        super().__init__(self.METHOD)


get_updates = GetUpdates()


__all__ = [
    'get_updates',
]
