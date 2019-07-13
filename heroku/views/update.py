from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

import logging

from heroku.models import Update, Message, Chat, User, Photo, Document, TextEntity, Text


LOGGER = logging.getLogger('heroku.update_view')


class UpdateView(APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._objects_to_save = []

    def _postpone_object_creation(self, model, **kwargs):
        result = model.objects.get_or_none(**kwargs)
        if result is None:
            result = model(**kwargs)
            self._objects_to_save.append(result)
        return result

    def _save_postponed_objects(self):
        objects_to_process = list(reversed(self._objects_to_save))
        while len(objects_to_process) > 0:
            objects_to_process.pop().save()

    def _process_text(self, text):
        LOGGER.info('[Update] Process text')

    def _process_photo(self, photo):
        LOGGER.info('[Update] Process photo')

    def _process_document(self, document):
        LOGGER.info('[Update] Process document')

    def post(self, request):
        update = request.data

        LOGGER.info('[Update] Received update: %s', update)

        if update.get('message') is None:
            return Response(HTTP_404_NOT_FOUND)

        message = update['message']
        from_user = message['from']
        user_object = self._postpone_object_creation(
            User,
            id=from_user['id'],
            is_bot=from_user['is_bot'],
            first_name=from_user['first_name'],
            last_name=from_user.get('last_name', ''),
            username=from_user.get('username', ''),
        )

        chat = message['chat']
        chat_object = self._postpone_object_creation(Chat, id=chat['id'], type=chat['type'])

        text = message.get('text', '')
        if text:
            text_entities = message.get('caption_entities', [])
            entity_objects = []
            for entity in text_entities:
                entity_user = entity.get('user')
                if entity_user is not None:
                    entity_user_object = self._postpone_object_creation(
                        User,
                        id=entity_user['id'],
                        is_bot=entity_user['is_bot'],
                        first_name=entity_user['first_name'],
                        last_name=entity_user.get('last_name', ''),
                        username=entity_user.get('username', ''),
                    )
                else:
                    entity_user_object = None
                entity_objects.append(self._postpone_object_creation(
                    TextEntity,
                    type=TextEntity.Type(entity['type']),
                    offset=entity['offset'],
                    length=entity['length'],
                    url=entity.get('url', ''),
                    user=entity_user_object,
                ))
            text_object = self._postpone_object_creation(
                Text,
                text=text,
                text_entities=entity_objects,
            )
        else:
            text_object = None

        photos = message.get('photo', [])
        if photos:
            max_sized_photo = photos[0]
            for photo in photos:
                if max_sized_photo['width'] * max_sized_photo['height'] < photo['width'] * photo['height']:
                    max_sized_photo = photo
            photo_object = self._postpone_object_creation(
                Photo,
                file_id=max_sized_photo['file_id'],
                width=max_sized_photo['width'],
                height=max_sized_photo['height'],
                file_size=max_sized_photo.get('file_size'),
            )
        else:
            photo_object = None

        document = message.get('document')
        if document:
            thumb = document.get('thumb')
            if thumb:
                thumb_object = self._postpone_object_creation(
                    Photo,
                    file_id=thumb['file_id'],
                    width=thumb['width'],
                    height=thumb['height'],
                    file_size=thumb.get('file_size'),
                )
            else:
                thumb_object = None
            document_object = self._postpone_object_creation(
                Document,
                file_id=document['file_id'],
                thumb=thumb_object,
                file_name=document.get('file_name', ''),
                mime_type=document.get('mime_type', ''),
                file_size=document.get('file_size'),
            )
        else:
            document_object = None

        message_object = self._postpone_object_creation(
            Message,
            message_id=message['message_id'],
            from_user=user_object,
            date=datetime.fromtimestamp(message['date']),
            chat=chat_object,
            text=text_object,
            photo=photo_object,
            document=document_object,
        )
        self._postpone_object_creation(Update, update_id=update['update_id'], message=message_object)

        if text:
            self._process_text(text_object)
        if photo_object:
            self._process_photo(photo_object)
        if document_object is not None:
            self._process_document(document_object)

        self._save_postponed_objects()

        return Response(status=HTTP_200_OK)
