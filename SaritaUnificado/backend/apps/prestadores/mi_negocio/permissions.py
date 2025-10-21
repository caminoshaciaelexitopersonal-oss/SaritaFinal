from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Permiso personalizado para permitir solo a los dueños de un objeto editarlo.
    Asume que el modelo tiene un campo 'perfil' que lo vincula al Perfil del prestador.
    """
    def has_object_permission(self, request, view, obj):
        # Los permisos de lectura están permitidos para cualquier solicitud,
        # por lo que siempre permitiremos las solicitudes GET, HEAD u OPTIONS.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # El permiso de escritura solo se concede al dueño del perfil.
        return obj.perfil == request.user.perfil_prestador
