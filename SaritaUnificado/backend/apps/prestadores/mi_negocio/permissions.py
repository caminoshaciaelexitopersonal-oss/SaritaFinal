# SaritaUnificado/backend/apps/prestadores/mi_negocio/permissions.py
from rest_framework import permissions

class IsOwnerAndPrestador(permissions.BasePermission):
    """
    Permiso personalizado para permitir solo a los dueños de un perfil de prestador
    editar o ver los objetos asociados.
    """
    def has_object_permission(self, request, view, obj):
        # Permisos de lectura están permitidos para cualquier solicitud,
        # así que siempre permitiremos GET, HEAD o OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True

        # El permiso de escritura solo se concede si el perfil del objeto
        # pertenece al usuario que realiza la solicitud.
        try:
            perfil_usuario = request.user.perfil_prestador
            return obj.perfil == perfil_usuario
        except AttributeError:
            # El usuario no tiene un perfil de prestador asociado.
            return False
