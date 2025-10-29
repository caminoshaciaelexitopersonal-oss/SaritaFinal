from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PlaceholderView(APIView):
    """
    Una vista marcador de posición que indica que el módulo está en desarrollo.
    """
    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)
