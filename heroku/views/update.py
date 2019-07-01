from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

import logging

LOGGER = logging.getLogger('heroku.update_view')


class UpdateView(APIView):
    def post(self, request):
        data = request.data
        LOGGER.info(type(data))
        LOGGER.info(data)

        return Response(status=HTTP_200_OK)
