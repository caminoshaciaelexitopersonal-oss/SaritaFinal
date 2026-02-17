import logging
from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from .models import (
    Vehicle, Conductor, ScheduledTrip, TransportBooking,
    TripLiquidation, TransportIncident, PassengerManifest
)
from apps.admin_plataforma.services.quintuple_erp import QuintupleERPService

logger = logging.getLogger(__name__)

class TransportService:
    """
    Motor Logístico de Transporte Turístico (Fase 13)
    """
    def __init__(self, user):
        self.user = user
        self.provider = user.perfil_prestador

    @transaction.atomic
    def programar_viaje(self, data):
        """
        Crea un viaje programado validando disponibilidad de recursos.
        """
        vehiculo_id = data.get('vehiculo_id')
        conductor_id = data.get('conductor_id')
        fecha = data['fecha_salida']
        hora = data['hora_salida']

        # 1. Validar conflicto de vehículo (Fase 13.3.1)
        if vehiculo_id:
            if self._verificar_conflicto_vehiculo(vehiculo_id, fecha, hora):
                raise ValueError("El vehículo ya está asignado a otro viaje en este horario.")

            # Verificar documentos (Fase 13.1.6)
            vehiculo = Vehicle.objects.get(id=vehiculo_id)
            if not self._validar_documentos_vehiculo(vehiculo):
                raise ValueError("El vehículo tiene documentación vencida o inválida.")

        # 2. Validar conflicto de conductor
        if conductor_id:
            if self._verificar_conflicto_conductor(conductor_id, fecha, hora):
                raise ValueError("El conductor ya tiene un viaje asignado en este horario.")

        trip = ScheduledTrip.objects.create(
            provider=self.provider,
            ruta_id=data['ruta_id'],
            fecha_salida=fecha,
            hora_salida=hora,
            vehiculo_id=vehiculo_id,
            conductor_id=conductor_id,
            capacidad_total=data['capacidad_total'],
            precio_por_pasajero=data['precio_por_pasajero'],
            estado=ScheduledTrip.TripStatus.PROGRAMADO
        )

        return trip

    def _verificar_conflicto_vehiculo(self, vehiculo_id, fecha, hora):
        conflicts = ScheduledTrip.objects.filter(
            vehiculo_id=vehiculo_id,
            fecha_salida=fecha,
            hora_salida=hora,
            estado__in=[ScheduledTrip.TripStatus.PROGRAMADO, ScheduledTrip.TripStatus.CONFIRMADO, ScheduledTrip.TripStatus.EN_TRANSITO]
        )
        if conflicts.exists():
            logger.debug(f"Conflicto Vehículo detectado. ID Existente: {conflicts.first().id}")
            return True
        return False

    def _verificar_conflicto_conductor(self, conductor_id, fecha, hora):
        return ScheduledTrip.objects.filter(
            conductor_id=conductor_id,
            fecha_salida=fecha,
            hora_salida=hora,
            estado__in=[ScheduledTrip.TripStatus.PROGRAMADO, ScheduledTrip.TripStatus.CONFIRMADO, ScheduledTrip.TripStatus.EN_TRANSITO]
        ).exists()

    def _validar_documentos_vehiculo(self, vehiculo):
        from django.utils import timezone
        today = timezone.now().date()

        # SOAT / Pólizas
        if vehiculo.insurance_expiry_date and vehiculo.insurance_expiry_date < today:
            return False

        # Certificaciones específicas
        invalid_certs = vehiculo.certifications.filter(expiry_date__lt=today, is_valid=True).exists()
        if invalid_certs:
            return False

        return True

    @transaction.atomic
    def registrar_reserva(self, trip_id, data_reserva):
        """
        Registra una reserva validando capacidad (Fase 13.1.4).
        """
        trip = ScheduledTrip.objects.select_for_update().get(id=trip_id, provider=self.provider)

        n_pasajeros = int(data_reserva['numero_pasajeros'])
        if trip.remaining_capacity() < n_pasajeros:
            raise ValueError(f"Capacidad insuficiente. Disponibles: {trip.remaining_capacity()}")

        reserva = TransportBooking.objects.create(
            provider=self.provider,
            trip=trip,
            cliente_ref_id=data_reserva['cliente_ref_id'],
            numero_pasajeros=n_pasajeros,
            total_pago=trip.precio_por_pasajero * n_pasajeros
        )

        # Actualizar capacidad
        trip.capacidad_reservada += n_pasajeros
        trip.save()

        # Generar manifiesto inicial si viene la data
        passengers = data_reserva.get('passengers', [])
        for p in passengers:
            PassengerManifest.objects.create(
                booking=reserva,
                nombre_completo=p['nombre'],
                documento_identidad=p['documento']
            )

        return reserva

    @transaction.atomic
    def actualizar_estado_viaje(self, trip_id, nuevo_estado):
        """
        Cambia el estado del viaje validando condiciones de seguridad.
        """
        trip = ScheduledTrip.objects.select_for_update().get(id=trip_id, provider=self.provider)

        if nuevo_estado == ScheduledTrip.TripStatus.EN_TRANSITO:
            # Validar documentos antes de iniciar (Fase 13.1.6)
            if not self._validar_documentos_vehiculo(trip.vehiculo):
                raise ValueError("No se puede iniciar: Vehículo con documentos vencidos.")

            if trip.conductor.estado != Conductor.ConductorStatus.ACTIVO:
                raise ValueError("No se puede iniciar: Conductor no activo.")

        trip.estado = nuevo_estado
        trip.save()
        return trip

    @transaction.atomic
    def liquidar_viaje(self, trip_id):
        """
        Realiza la liquidación financiera del viaje (Fase 13.1.5).
        """
        trip = ScheduledTrip.objects.select_for_update().get(id=trip_id, provider=self.provider)
        logger.debug(f"LIQUIDAR: Trip {trip.id}, Estado {trip.estado}")

        if trip.estado != ScheduledTrip.TripStatus.FINALIZADO:
            raise ValueError(f"Solo se pueden liquidar viajes finalizados. Estado actual: {trip.estado}")

        if hasattr(trip, 'liquidation'):
            raise ValueError("Este viaje ya ha sido liquidado.")

        total_ingresos = trip.bookings.filter(pagado=True).aggregate(t=models.Sum('total_pago'))['t'] or Decimal('0.00')
        total_comisiones = trip.comision_conductor # Asumimos fija o calculada previamente
        logger.debug(f"LIQUIDAR: Ingresos={total_ingresos}, Comisiones={total_comisiones}")

        try:
            liq = TripLiquidation.objects.create(
                provider=self.provider,
                trip=trip,
                total_ingresos=total_ingresos,
                total_comisiones=total_comisiones,
                utilidad_neta=total_ingresos - total_comisiones
            )
            logger.info(f"LIQUIDAR: Liquidation creada ID {liq.id}")
        except Exception as e:
            logger.error(f"LIQUIDAR ERROR CREATING LIQ: {e}")
            raise e

        trip.estado = ScheduledTrip.TripStatus.LIQUIDADO
        trip.save()

        # IMPACTO ERP
        erp_service = QuintupleERPService(user=self.user)
        payload = {
            "perfil_id": str(self.provider.id),
            "amount": float(total_ingresos),
            "description": f"Liquidación Viaje {trip.ruta.nombre} - {trip.fecha_salida}",
            "trip_id": str(trip.id)
        }
        impact = erp_service.record_impact("TRANSPORT_TRIP_LIQUIDATED", payload)

        contable_id = impact.get('contable_id')
        if contable_id and not str(contable_id).startswith("ERROR"):
            liq.asiento_contable_ref_id = contable_id

        liq.save()

        return liq

from django.db import models
