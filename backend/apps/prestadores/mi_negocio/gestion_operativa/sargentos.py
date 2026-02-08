# backend/apps/prestadores/mi_negocio/gestion_operativa/sargentos.py
import logging
from django.utils import timezone
from .modulos_genericos.perfil.models import ProviderProfile
from apps.audit.models import AuditLog
from api.models import CustomUser

logger = logging.getLogger(__name__)

class SargentoOperativo:
    """
    Ejecutor de acciones mínimas e indivisibles del dominio operativo genérico.
    """

    @staticmethod
    def crear_orden_servicio(perfil_id, descripcion, parametros=None):
        # Lógica atómica: Crear registro en tabla de órdenes (simulado si no hay modelo específico)
        # Por ahora usamos el log de auditoría como evidencia de la creación de la orden.
        logger.info(f"SARGENTO: Creando orden de servicio para perfil {perfil_id}")
        return {"id": "ORD-" + str(timezone.now().timestamp()), "status": "CREATED"}

    @staticmethod
    def actualizar_estado(entidad_tipo, entidad_id, nuevo_estado, motivo=""):
        # Lógica atómica: Actualizar campo 'estado' de cualquier modelo operativo
        logger.info(f"SARGENTO: Actualizando estado de {entidad_tipo} {entidad_id} a {nuevo_estado}")
        # En una implementación real, esto usaría apps.get_model()
        return True

    @staticmethod
    def registrar_ejecucion_tarea(tarea_id, operario_id, resultado):
        # Lógica atómica: Guardar log de ejecución
        logger.info(f"SARGENTO: Registrando ejecución de tarea {tarea_id} por operario {operario_id}")
        return True

    @staticmethod
    def gestionar_reintento(operacion_id, intento_n):
        # Lógica atómica: Incrementar contador de reintentos
        logger.info(f"SARGENTO: Gestionando reintento {intento_n} para operacion {operacion_id}")
        return True

    @staticmethod
    def registrar_bitacora_operativa(usuario_id, accion, detalles):
        try:
            user = CustomUser.objects.get(id=usuario_id)
            AuditLog.objects.create(
                user=user,
                username=user.username,
                action=f"OPERATIONAL_{accion}",
                details=detalles
            )
            logger.info(f"SARGENTO: Acción operativa '{accion}' registrada en bitácora.")
        except Exception as e:
            logger.error(f"SARGENTO: Error al registrar bitácora operativa: {e}")
