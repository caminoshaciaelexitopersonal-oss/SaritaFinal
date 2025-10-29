from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Empleado, ConceptoNomina, Nomina
from .serializers import (
    EmpleadoSerializer,
    ConceptoNominaSerializer,
    NominaSerializer,
    NominaProcesarSerializer,
)
from apps.prestadores.models import Perfil
from .services import procesar_nomina_service

class EmpleadoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar los empleados de un prestador.
    """
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filtra los empleados para que solo pertenezcan al perfil del usuario autenticado.
        """
        perfil = Perfil.objects.get(usuario=self.request.user)
        return Empleado.objects.filter(perfil=perfil)

    def perform_create(self, serializer):
        """
        Asigna automáticamente el perfil del prestador al crear un empleado.
        """
        perfil = Perfil.objects.get(usuario=self.request.user)
        serializer.save(perfil=perfil)


class ConceptoNominaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar los conceptos de nómina.

    Por ahora, se asume que los conceptos son globales.
    En el futuro, podrían pertenecer a un prestador específico.
    """
    queryset = ConceptoNomina.objects.all()
    serializer_class = ConceptoNominaSerializer
    permission_classes = [IsAuthenticated]


class NominaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para consultar nóminas y procesar nuevas corridas.
    """
    serializer_class = NominaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filtra las nóminas para que solo pertenezcan al perfil del usuario autenticado.
        """
        perfil = Perfil.objects.get(usuario=self.request.user)
        return Nomina.objects.filter(perfil=perfil)

    @action(detail=False, methods=['post'], serializer_class=NominaProcesarSerializer)
    def procesar(self, request):
        """
        Acción para crear y procesar una nueva corrida de nómina.
        Utiliza un servicio para encapsular la lógica de negocio.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        fecha_inicio = serializer.validated_data['fecha_inicio']
        fecha_fin = serializer.validated_data['fecha_fin']
        perfil = Perfil.objects.get(usuario=self.request.user)

        try:
            # Llamada al servicio que encapsula la lógica de negocio
            nomina_procesada = procesar_nomina_service(
                perfil=perfil,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin
            )

            # Serializar el resultado para la respuesta
            resultado_serializer = NominaSerializer(nomina_procesada)
            return Response(resultado_serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"error": f"Ocurrió un error al procesar la nómina: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )
