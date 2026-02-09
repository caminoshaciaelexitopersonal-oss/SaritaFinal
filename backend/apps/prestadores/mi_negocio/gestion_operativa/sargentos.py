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
        from .models import OrdenOperativa
        from django.utils import timezone
        import uuid

        orden = OrdenOperativa.objects.create(
            provider_id=perfil_id,
            contrato_ref_id=parametros.get("contrato_id", uuid.uuid4()),
            descripcion_servicio=descripcion,
            fecha_inicio=timezone.now(),
            fecha_fin_estimada=timezone.now() + timezone.timedelta(days=1),
            estado=OrdenOperativa.EstadoOrden.PENDIENTE
        )
        logger.info(f"SARGENTO: Orden operativa {orden.id} creada.")
        return {"id": str(orden.id), "status": "CREATED"}

    @staticmethod
    def actualizar_estado(entidad_tipo, entidad_id, nuevo_estado, motivo="", agente_id=None):
        from django.apps import apps
        from .models import OrdenOperativa, RegistroOperativo

        # Lógica atómica: Actualizar campo 'estado'
        logger.info(f"SARGENTO: Actualizando estado de {entidad_tipo} {entidad_id} a {nuevo_estado}")

        if entidad_tipo == "OrdenOperativa":
            orden = OrdenOperativa.objects.get(id=entidad_id)
            estado_anterior = orden.estado
            orden.estado = nuevo_estado
            orden.save()

            # REGISTRO OBLIGATORIO EN BITÁCORA
            RegistroOperativo.objects.create(
                orden=orden,
                estado_anterior=estado_anterior,
                estado_nuevo=nuevo_estado,
                agente_responsable_id=agente_id or uuid.uuid4(), # Fallback si no viene agente
                observaciones=motivo
            )
            return True

        return False

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
    def registrar_costo_operativo(perfil_id, orden_id, concepto, monto):
        from .modulos_genericos.costos.models import Costo
        costo = Costo.objects.create(
            perfil_id=perfil_id,
            orden_operativa_ref_id=orden_id,
            concepto=concepto,
            monto=monto,
            fecha=timezone.now().date()
        )
        logger.info(f"SARGENTO: Costo {costo.id} registrado para orden {orden_id}.")
        return str(costo.id)

    @staticmethod
    def asignar_recurso(orden_id, item_id, cantidad):
        from .modulos_genericos.inventario.models import AsignacionRecurso, InventoryItem
        item = InventoryItem.objects.get(id=item_id)
        asignacion = AsignacionRecurso.objects.create(
            item=item,
            orden_operativa_ref_id=orden_id,
            cantidad_asignada=cantidad
        )
        # Bloquear stock (simplificado)
        item.cantidad -= cantidad
        item.save()
        logger.info(f"SARGENTO: Recurso {item_id} asignado a orden {orden_id}.")
        return str(asignacion.id)

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
