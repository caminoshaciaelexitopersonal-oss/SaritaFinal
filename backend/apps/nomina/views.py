from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Empleado, ConceptoNomina, Nomina
from .serializers import EmpleadoSerializer, ConceptoNominaSerializer, NominaSerializer, NominaProcesarSerializer
from apps.prestadores.models import Perfil
from .services import procesar_nomina_service

class EmpleadoViewSet(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Empleado.objects.filter(perfil=self.request.user.perfil_prestador)
    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

class ConceptoNominaViewSet(viewsets.ModelViewSet):
    queryset = ConceptoNomina.objects.all()
    serializer_class = ConceptoNominaSerializer
    permission_classes = [IsAuthenticated]

class NominaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NominaSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Nomina.objects.filter(perfil=self.request.user.perfil_prestador)
    @action(detail=False, methods=['post'], serializer_class=NominaProcesarSerializer)
    def procesar(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            nomina_procesada = procesar_nomina_service(
                perfil=request.user.perfil_prestador,
                fecha_inicio=serializer.validated_data['fecha_inicio'],
                fecha_fin=serializer.validated_data['fecha_fin']
            )
            return Response(NominaSerializer(nomina_procesada).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
