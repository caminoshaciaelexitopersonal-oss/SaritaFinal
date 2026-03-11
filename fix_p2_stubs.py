import os
import re

def replace_in_file(filepath, search_pattern, replacement):
    with open(filepath, 'r') as f:
        content = f.read()
    new_content = re.sub(search_pattern, replacement, content, flags=re.MULTILINE|re.DOTALL)
    with open(filepath, 'w') as f:
        f.write(new_content)

# 1. Port full logic in registrar_reserva_paquete
agency_logic = """    @transaction.atomic
    def registrar_reserva_paquete(self, package_id, data_reserva):
        \"\"\"
        Reserva un paquete consolidado (Fase 14.1.5).
        \"\"\"
        package = TravelPackage.objects.select_for_update().get(id=package_id, provider=self.provider)

        if package.estado == TravelPackage.PackageStatus.LIQUIDADO:
            raise ValueError("No se puede reservar un paquete ya liquidado.")

        n_personas = int(data_reserva['numero_personas'])
        total_pago = package.precio_total * Decimal(str(n_personas))

        booking = AgencyBooking.objects.create(
            provider=self.provider,
            package=package,
            cliente_ref_id=data_reserva['cliente_ref_id'],
            fecha_inicio=data_reserva['fecha_inicio'],
            numero_personas=n_personas,
            total_facturado=total_pago,
            status=AgencyBooking.BookingStatus.CONFIRMED
        )

        # IMPACTO ERP (Decoupled vía EventBus)
        EventBus.emit(\"ERP_IMPACT_REQUESTED\", {
            \"event_type\": \"AGENCY_PACKAGE_BOOKING\",
            \"payload\": {
                \"booking_id\": str(booking.id),
                \"amount\": float(total_pago),
                \"description\": f\"Reserva Paquete: {package.nombre}\"
            },
            \"user_id\": self.user.id
        })

        return booking"""

replace_in_file('backend/apps/prestadores/mi_negocio/operativa_turistica/operadores_directos/agencias/services.py',
                r'    @transaction\.atomic\s+def registrar_reserva_paquete\(self, package_id, data_reserva\):.*?return booking',
                agency_logic)

print("Priority 2 stubs implemented.")
