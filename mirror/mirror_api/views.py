from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException


class MirrorView(APIView):
    def get(self, request):
        try:
            text = self.request.query_params.get('text')
            if len(text) == 0:
                return Response('No text was entered')
            else:
                response = {
                    'text': str(text)
                }
            return Response(response)
        except APIException:
            return APIException('Any text needed')
