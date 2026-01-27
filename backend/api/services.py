from backend.api.models import Publicacion, CustomUser
from rest_framework.exceptions import PermissionDenied, ValidationError

def aprobar_publicacion(publicacion_id: int, usuario: CustomUser) -> Publicacion:
    """
    Aprueba una publicación, moviéndola al siguiente estado en el flujo de trabajo.
    - Un FUNCIONARIO_DIRECTIVO la mueve de PENDIENTE_DIRECTIVO a PENDIENTE_ADMIN.
    - Un ADMIN la mueve de PENDIENTE_ADMIN a PUBLICADO.
    """
    try:
        publicacion = Publicacion.objects.get(pk=publicacion_id)
    except Publicacion.DoesNotExist:
        raise ValidationError(f"La publicación con id {publicacion_id} no existe.")

    if publicacion.estado == 'PENDIENTE_DIRECTIVO' and usuario.role == CustomUser.Role.FUNCIONARIO_DIRECTIVO:
        publicacion.estado = 'PENDIENTE_ADMIN'
    elif publicacion.estado == 'PENDIENTE_ADMIN' and usuario.role == CustomUser.Role.ADMIN:
        publicacion.estado = 'PUBLICADO'
    else:
        raise PermissionDenied("No tiene permiso para realizar esta acción o la publicación no está en el estado correcto.")

    publicacion.save()
    return publicacion

def rechazar_publicacion(publicacion_id: int, usuario: CustomUser) -> Publicacion:
    """
    Rechaza una publicación y la devuelve al estado BORRADOR.
    Solo puede ser ejecutado por un ADMIN o FUNCIONARIO_DIRECTIVO.
    """
    if not (usuario.role == CustomUser.Role.ADMIN or usuario.role == CustomUser.Role.FUNCIONARIO_DIRECTIVO):
        raise PermissionDenied("No tiene permiso para realizar esta acción.")

    try:
        publicacion = Publicacion.objects.get(pk=publicacion_id)
    except Publicacion.DoesNotExist:
        raise ValidationError(f"La publicación con id {publicacion_id} no existe.")

    publicacion.estado = 'BORRADOR'
    publicacion.save()
    return publicacion

def enviar_para_aprobacion(publicacion_id: int, usuario: CustomUser) -> Publicacion:
    """
    Envía una publicación para su aprobación, moviéndola al estado PENDIENTE_DIRECTIVO.
    El usuario debe ser el autor de la publicación o un funcionario.
    """
    try:
        publicacion = Publicacion.objects.get(pk=publicacion_id)
    except Publicacion.DoesNotExist:
        raise ValidationError(f"La publicación con id {publicacion_id} no existe.")

    # Un funcionario puede enviar cualquier publicación para aprobación.
    # Un autor solo puede enviar sus propias publicaciones.
    es_funcionario = usuario.role in [CustomUser.Role.ADMIN, CustomUser.Role.FUNCIONARIO_DIRECTIVO, CustomUser.Role.FUNCIONARIO_PROFESIONAL]
    es_autor = publicacion.autor == usuario

    if not (es_funcionario or es_autor):
        raise PermissionDenied("No tiene permiso para enviar esta publicación para aprobación.")

    publicacion.estado = 'PENDIENTE_DIRECTIVO'
    publicacion.save()
    return publicacion
