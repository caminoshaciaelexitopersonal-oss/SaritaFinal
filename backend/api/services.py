from .models import Publicacion, CustomUser
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

import hashlib
import json
from apps.audit.models import ForensicSecurityLog
from rest_framework.authtoken.models import Token
import logging

logger = logging.getLogger(__name__)

class DefenseService:
    """
    Servicio Central de Contención y Defensa S-0.3.
    Responsable de neutralizar ataques y registrar evidencia forense.
    """

    @staticmethod
    def neutralize_threat(user, attack_vector, payload, headers, threat_level='HIGH'):
        """
        Neutraliza una amenaza activa mediante cuarentena y registro forense.
        """
        source_ip = headers.get('REMOTE_ADDR') or headers.get('HTTP_X_FORWARDED_FOR')

        # 1. Registro Forense Inmediato
        log_entry = ForensicSecurityLog.objects.create(
            user=user if user and not user.is_anonymous else None,
            source_ip=source_ip,
            threat_level=threat_level,
            attack_vector=attack_vector,
            payload_captured=payload,
            headers_captured={k: v for k, v in headers.items() if isinstance(v, str)},
            action_taken="SESSION_QUARANTINE, TOKEN_INVALIDATED" if user and not user.is_anonymous else "IP_BLOCK_RECOMMENDED"
        )

        # 2. Firmar registro forense (Integridad RC-S)
        payload_str = f"{log_entry.id}{log_entry.timestamp}{attack_vector}{json.dumps(payload)}"
        log_entry.integrity_hash = hashlib.sha256(payload_str.encode()).hexdigest()
        log_entry.save()

        # 3. Contención: Invalidar Sesión si hay usuario
        if user and not user.is_anonymous:
            # Eliminar todos los tokens del usuario para forzar logout global
            Token.objects.filter(user=user).delete()
            logger.warning(f"S-0: Usuario {user.username} puesto en CUARENTENA por {attack_vector}.")

        # 4. Notificar al Sovereignty Center (vía Logs por ahora)
        logger.error(f"S-0 CRITICAL: Ataque detectado y contenido. Vector: {attack_vector}. IP: {source_ip}")

        return log_entry.id
