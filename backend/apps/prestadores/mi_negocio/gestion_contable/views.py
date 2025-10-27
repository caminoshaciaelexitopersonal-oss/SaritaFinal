from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class PlaceholderViewSet(ViewSet):
    """
    ViewSet de marcador de posición que devuelve una respuesta vacía.
    Esto evita errores 404 en el frontend para módulos en desarrollo.
    """
    def list(self, request):
        return Response([])

    def create(self, request):
        return Response({"message": "Módulo en desarrollo"}, status=201)

    def retrieve(self, request, pk=None):
        return Response({"message": "Módulo en desarrollo"})

    def update(self, request, pk=None):
        return Response({"message": "Módulo en desarrollo"})

    def partial_update(self, request, pk=None):
        return Response({"message": "Módulo en desarrollo"})

    def destroy(self, request, pk=None):
        return Response(status=204)
