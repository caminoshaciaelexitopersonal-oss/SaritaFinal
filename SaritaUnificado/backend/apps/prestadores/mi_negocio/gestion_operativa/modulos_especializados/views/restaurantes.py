# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/views/restaurantes.py
from ...modulos_genericos.views.base import GenericViewSet
from apps.prestadores.models import CategoriaMenu, ProductoMenu, Mesa, ReservaMesa
from ..serializers.restaurantes import CategoriaMenuSerializer, ProductoMenuSerializer, MesaSerializer, ReservaMesaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class CategoriaMenuViewSet(GenericViewSet):
    queryset = CategoriaMenu.objects.all()
    serializer_class = CategoriaMenuSerializer

class ProductoMenuViewSet(GenericViewSet):
    queryset = ProductoMenu.objects.all()
    serializer_class = ProductoMenuSerializer

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil_prestador'):
            return ProductoMenu.objects.filter(categoria__perfil=user.perfil_prestador)
        return ProductoMenu.objects.none()

    def perform_create(self, serializer):
        categoria = serializer.validated_data.get('categoria')
        if categoria.perfil == self.request.user.perfil_prestador:
            serializer.save()
        else:
            raise serializers.ValidationError("No tiene permiso para añadir productos a esta categoría.")

class MesaViewSet(GenericViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class ReservaMesaViewSet(GenericViewSet):
    queryset = ReservaMesa.objects.all()
    serializer_class = ReservaMesaSerializer

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil_prestador'):
            return ReservaMesa.objects.filter(mesa__perfil=user.perfil_prestador)
        return ReservaMesa.objects.none()

    def perform_create(self, serializer):
        mesa = serializer.validated_data.get('mesa')
        if mesa.perfil == self.request.user.perfil_prestador:
            serializer.save()
        else:
            raise serializers.ValidationError("No tiene permiso para crear una reserva en esta mesa.")
