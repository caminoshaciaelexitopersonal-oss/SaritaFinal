from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from api.permissions import IsSuperAdmin
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from apps.admin_plataforma.gestion_operativa.modulos_genericos.valoraciones.models import Valoracion
from .serializers import ValoracionSerializer, RespuestaPrestadorSerializer

class ValoracionViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @action(detail=True, methods=['patch'], url_path='responder', serializer_class=RespuestaPrestadorSerializer)
    def responder(self, request, pk=None):
        valoracion = self.get_object()
        serializer = self.get_serializer(valoracion, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(fecha_respuesta=timezone.now())
        full_serializer = ValoracionSerializer(valoracion)
        return Response(full_serializer.data)
