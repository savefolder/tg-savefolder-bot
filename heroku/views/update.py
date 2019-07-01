from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

import logging

from heroku.models import Update, Message, Chat, User


LOGGER = logging.getLogger('heroku.update_view')


class UpdateView(APIView):
    def post(self, request):
        update = request.data

        LOGGER.debug('[Update] Recieved update: $s', update)

        if update.get('message') is not None:
            message = update['message']
            from_user = message['from']
            user_object = User.objects.get_or_create(
                id=from_user['id'],
                is_bot=from_user['is_bot'],
                first_name=from_user['first_name'],
                last_name=from_user.get('last_name'),
                username=from_user.get('username'),
            )
            chat = message['chat']
            chat_object = Chat.objects.get_or_create(id=chat['id'], chat_type=chat['type'])
            text = message.get('text', '')
            message_object = Message.objects.create(
                message_id=message['message_id'],
                from_user=user_object,
                date=datetime.fromtimestamp(message['date']),
                chat=chat_object,
                text=text,
            )
            Update.objects.create(update_id=update['update_id'], message=message_object)

        return Response(status=HTTP_200_OK)
