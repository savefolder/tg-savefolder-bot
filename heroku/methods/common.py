from heroku.methods.method import TelegramAPIMethod


class GetMe(TelegramAPIMethod):
    METHOD = 'getMe'

    def __init__(self):
        super().__init__(self.METHOD)


get_me = GetMe()


__all__ = [
    'get_me',
]
