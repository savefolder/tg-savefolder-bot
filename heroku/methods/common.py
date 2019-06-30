from .method import TelegramAPIMethod


class GetMe(TelegramAPIMethod):
    METHOD = 'getMe'

    def __init__(self):
        super().__init__(self.METHOD)


get_me = GetMe()


class SetWebhook(TelegramAPIMethod):
    METHOD = 'setWebhook'

    def __init__(self):
        super().__init__(self.METHOD)


set_webhook = SetWebhook()


class DeleteWebhook(TelegramAPIMethod):
    METHOD = 'deleteWebhook'

    def __init__(self):
        super().__init__(self.METHOD)


delete_webhook = DeleteWebhook()


__all__ = [
    'get_me',
    'set_webhook',
    'delete_webhook',
]
