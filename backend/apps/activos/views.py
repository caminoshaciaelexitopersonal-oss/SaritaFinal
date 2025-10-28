# backend/apps/activos/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ActivoFijo
from .serializers import ActivoFijoSerializer, RegistroDepreciacionSerializer
from api.permissions import IsOwnerOrReadOnly

class ActivoFijoViewSet(viewsets.ModelViewSet):
    queryset = ActivoFijo.objects.all()
    serializer_class = ActivoFijoSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

    @action(detail=True, methods=['get'])
    def depreciaciones(self, request, pk=None):
        activo = self.get_object()
        registros = activo.registros_depreciacion.all().order_by('-fecha')
        serializer = RegistroDepreciacionSerializer(registros, many=True)
        return Response(serializer.data)
