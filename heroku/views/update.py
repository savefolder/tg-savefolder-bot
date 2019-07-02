from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

import logging

from heroku.models import Update, Message, Chat, User, Photo, Document


LOGGER = logging.getLogger('heroku.update_view')


class UpdateView(APIView):
    def post(self, request):
        update = request.data

        LOGGER.info('[Update] Received update: $s', update)

        if update.get('message') is not None:
            message = update['message']
            from_user = message['from']
            user_object, _ = User.objects.get_or_create(
                id=from_user['id'],
                is_bot=from_user['is_bot'],
                first_name=from_user['first_name'],
                last_name=from_user.get('last_name'),
                username=from_user.get('username'),
            )
            chat = message['chat']
            chat_object, _ = Chat.objects.get_or_create(id=chat['id'], chat_type=chat['type'])

            text = message.get('text', '')

            photos = message.get('photo', [])
            photos_list = [
                Photo.objects.create(
                    file_id=photo['file_id'],
                    width=photo['width'],
                    height=photo['height'],
                    file_size=photo.get('file_size'),
                )
                for photo in photos
            ]

            document = message.get('document', None)
            if document:
                thumb = document.get('thumb')
                if thumb:
                    thumb_object = Photo.objects.create(
                        file_id=thumb['file_id'],
                        width=thumb['width'],
                        height=thumb['height'],
                        file_size=thumb.get('file_size'),
                    )
                else:
                    thumb_object = None
                document_object = Document.objects.create(
                    file_id=document['file_id'],
                    thumb=thumb_object,
                    file_name=document.get('filename'),
                    mime_type=document.get('mime_type'),
                    file_size=document.get('file_size'),
                )
            else:
                document_object = None

            message_object = Message.objects.create(
                message_id=message['message_id'],
                from_user=user_object,
                date=datetime.fromtimestamp(message['date']),
                chat=chat_object,
                text=text,
                photos=photos_list,
                document=document_object,
            )
            Update.objects.create(update_id=update['update_id'], message=message_object)

            if text:
                self._process_text(text)
            if photos_list:
                self._process_photos(photos_list)
            if document_object is not None:
                self._process_document(document_object)

        return Response(status=HTTP_200_OK)

    def _process_text(self, text):
        LOGGER.info('[Update] Process text')
        pass

    def _process_photos(self, photos_list):
        LOGGER.info('[Update] Process photos')
        pass

    def _process_document(self, document):
        LOGGER.info('[Update] Process document')
        pass
