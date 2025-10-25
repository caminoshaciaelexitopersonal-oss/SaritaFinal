# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/permissions.py
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Permiso personalizado para permitir solo a los dueños de un objeto editarlo.
    """
    def has_object_permission(self, request, view, obj):
        # Los permisos de lectura están permitidos para cualquier solicitud,
        # así que siempre permitiremos GET, HEAD o OPTIONS.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # El permiso de escritura solo se concede al dueño del perfil.
        return obj.perfil == request.user.perfil_prestador
