from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
 
from .models import Perfil
 
from api.serializers import AdminPrestadorSerializer
from api.permissions import IsAdminOrFuncionario

class AdminPrestadorViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = AdminPrestadorSerializer
    permission_classes = [IsAdminOrFuncionario]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['estado']

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        prestador = self.get_object()
        prestador.estado = 'Activo'
        prestador.save()
        return Response({'status': 'Prestador aprobado'})
