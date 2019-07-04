from heroku.methods.method import TelegramAPIMethod


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


class GetWebHookInfo(TelegramAPIMethod):
    METHOD = 'getWebhookInfo'

    def __init__(self):
        super().__init__(self.METHOD)


get_webhook_info = GetWebHookInfo()


__all__ = [
    'set_webhook',
    'delete_webhook',
    'get_webhook_info',
]
