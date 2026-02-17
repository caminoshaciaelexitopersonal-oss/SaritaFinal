import logging
from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from .models import (
    GuiaTuristico, ServicioGuiado, LiquidacionGuia, IncidenciaServicio, CertificacionGuia
)
from apps.admin_plataforma.services.quintuple_erp import QuintupleERPService

logger = logging.getLogger(__name__)

class GuideService:
    """
    Motor Operativo para Guías Turísticos (Fase 12)
    """
    def __init__(self, user):
        self.user = user
        self.provider = user.perfil_prestador

    @transaction.atomic
    def programar_servicio(self, data):
        """
        Programa un nuevo servicio guiado.
        """
        # Validación preventiva de conflictos (Fase 12.4.2)
        guia_id = data.get('guia_asignado_id')
        if guia_id:
            if self._verificar_conflicto_horario(guia_id, data['fecha'], data['hora_inicio']):
                raise ValueError("El guía ya tiene un servicio asignado en ese horario.")

        servicio = ServicioGuiado.objects.create(
            provider=self.provider,
            ruta_id=data['ruta_id'],
            fecha=data['fecha'],
            hora_inicio=data['hora_inicio'],
            grupo_id=data['grupo_id'],
            guia_asignado_id=guia_id,
            precio_total=data.get('precio_total', 0),
            estado=ServicioGuiado.Estado.PROGRAMADO
        )

        return servicio

    def _verificar_conflicto_horario(self, guia_id, fecha, hora_inicio):
        # Simplificado: asume que cada tour dura 4 horas
        return ServicioGuiado.objects.filter(
            guia_asignado_id=guia_id,
            fecha=fecha,
            hora_inicio=hora_inicio,
            estado__in=[ServicioGuiado.Estado.PROGRAMADO, ServicioGuiado.Estado.CONFIRMADO, ServicioGuiado.Estado.EN_CURSO]
        ).exists()

    @transaction.atomic
    def liquidar_servicio(self, servicio_id, data_liquidacion):
        """
        Finaliza el servicio y calcula la comisión del guía.
        """
        servicio = ServicioGuiado.objects.select_for_update().get(id=servicio_id, provider=self.provider)

        if servicio.estado == ServicioGuiado.Estado.LIQUIDADO:
            raise ValueError("El servicio ya ha sido liquidado.")

        # Lógica de Comisión (12.1.4)
        tipo_comision = data_liquidacion.get('tipo', 'PORCENTAJE')
        valor = Decimal(str(data_liquidacion.get('valor', 10)))

        if tipo_comision == 'PORCENTAJE':
            servicio.comision_guia = servicio.precio_total * (valor / 100)
        else:
            servicio.comision_guia = valor

        servicio.estado = ServicioGuiado.Estado.LIQUIDADO
        servicio.save()

        # IMPACTO ERP (Comercial y Contable)
        erp_service = QuintupleERPService(user=self.user)
        payload = {
            "perfil_id": str(self.provider.id),
            "amount": float(servicio.precio_total),
            "description": f"Servicio Guiado Finalizado - {servicio.ruta.nombre}",
            "comision_guia": float(servicio.comision_guia)
        }

        impact = erp_service.record_impact("GUIDED_SERVICE_COMPLETED", payload)

        return impact

    @transaction.atomic
    def reportar_incidencia(self, servicio_id, descripcion, gravedad):
        servicio = ServicioGuiado.objects.get(id=servicio_id, provider=self.provider)

        incidencia = IncidenciaServicio.objects.create(
            provider=self.provider,
            servicio=servicio,
            descripcion=descripcion,
            gravedad=gravedad,
            staff_reporta=self.user
        )

        # Si la gravedad es alta o crítica, suspender guía preventivamente (Fase 12.1.5)
        if gravedad in [IncidenciaServicio.Gravedad.ALTA, IncidenciaServicio.Gravedad.CRITICA]:
            if servicio.guia_asignado:
                servicio.guia_asignado.estado = GuiaTuristico.Estado.SUSPENDIDO
                servicio.guia_asignado.save()
                logger.warning(f"GUÍA SUSPENDIDO: {servicio.guia_asignado.usuario.username} por incidencia crítica.")

        return incidencia
