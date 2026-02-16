from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    GuiaTuristico, CertificacionGuia, LocalRutaTuristica, Itinerario,
    GrupoTuristico, ServicioGuiado, LiquidacionGuia, IncidenciaServicio, Skill
)
from .serializers import *

class GuiaBaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.model.objects.filter(provider=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        serializer.save(provider=self.request.user.perfil_prestador)

class GuiaTuristicoViewSet(GuiaBaseViewSet):
    model = GuiaTuristico
    serializer_class = GuiaTuristicoSerializer

class CertificacionGuiaViewSet(GuiaBaseViewSet):
    model = CertificacionGuia
    serializer_class = CertificacionGuiaSerializer

class LocalRutaTuristicaViewSet(GuiaBaseViewSet):
    model = LocalRutaTuristica
    serializer_class = LocalRutaTuristicaSerializer

class ItinerarioViewSet(viewsets.ModelViewSet):
    queryset = Itinerario.objects.all()
    serializer_class = ItinerarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class GrupoTuristicoViewSet(GuiaBaseViewSet):
    model = GrupoTuristico
    serializer_class = GrupoTuristicoSerializer

class ServicioGuiadoViewSet(GuiaBaseViewSet):
    model = ServicioGuiado
    serializer_class = ServicioGuiadoSerializer

    @action(detail=True, methods=['post'])
    def confirmar(self, request, pk=None):
        servicio = self.get_object()
        # Verificar guía y certificaciones
        if not servicio.guia_asignado:
            return Response({'error': 'No hay guía asignado'}, status=status.HTTP_400_BAD_REQUEST)

        certificaciones_validas = any(c.is_valid() for c in servicio.guia_asignado.certificaciones.all())
        if not certificaciones_validas:
             return Response({'error': 'El guía no tiene certificaciones válidas'}, status=status.HTTP_400_BAD_REQUEST)

        servicio.estado = ServicioGuiado.Estado.CONFIRMADO
        servicio.save()
        return Response({'status': 'Servicio confirmado'})

class LiquidacionGuiaViewSet(GuiaBaseViewSet):
    model = LiquidacionGuia
    serializer_class = LiquidacionGuiaSerializer

class IncidenciaServicioViewSet(GuiaBaseViewSet):
    model = IncidenciaServicio
    serializer_class = IncidenciaServicioSerializer

class SkillViewSet(GuiaBaseViewSet):
    model = Skill
    serializer_class = SkillSerializer
