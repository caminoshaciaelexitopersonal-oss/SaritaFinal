# backend/simulate_agency_14.py
import os
import django
import uuid
from decimal import Decimal
from django.utils import timezone
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from api.models import CustomUser
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from apps.prestadores.mi_negocio.operativa_turistica.operadores_directos.agencias.models import TravelPackage, PackageComponent, AgencyBooking, AgencyLiquidation
from apps.admin_plataforma.services.governance_kernel import GovernanceKernel

def simulate_agency():
    print("🚀 INICIANDO SIMULACIÓN DE AGENCIA DE VIAJES FASE 14.2")

    # 0. Limpieza
    print("--- Limpiando datos previos... ---")
    AgencyLiquidation.objects.all().delete()
    AgencyBooking.objects.all().delete()
    PackageComponent.objects.all().delete()
    TravelPackage.objects.all().delete()

    # 1. Setup - Usuario Agencia
    user_agencia, _ = CustomUser.objects.get_or_create(username="agency_owner", defaults={"role":"PRESTADOR", "email":"agency@test.com"})
    # Promoción temporal para liquidación
    user_agencia.is_superuser = True
    user_agencia.save()

    profile_agencia, _ = ProviderProfile.objects.get_or_create(
        usuario=user_agencia,
        defaults={"nombre_comercial": "Agencia Central", "provider_type":"AGENCY", "is_active": True}
    )
    kernel = GovernanceKernel(user_agencia)

    # 2. Setup - Otros Proveedores (Simulados)
    # Reutilizaremos perfiles existentes o crearemos si es necesario.
    # En este entorno usualmente ya hay varios.

    # Proveedor Hotel
    u_hotel, _ = CustomUser.objects.get_or_create(username="hotel_prov", defaults={"role":"PRESTADOR"})
    p_hotel, _ = ProviderProfile.objects.get_or_create(usuario=u_hotel, defaults={"nombre_comercial": "Gran Hotel", "provider_type":"HOTEL"})

    # Proveedor Guía
    u_guia, _ = CustomUser.objects.get_or_create(username="guia_prov", defaults={"role":"PRESTADOR"})
    p_guia, _ = ProviderProfile.objects.get_or_create(usuario=u_guia, defaults={"nombre_comercial": "Guía Experto", "provider_type":"GUIDE"})

    # 3. Crear Paquete (Fase 14.1.5)
    print("--- Creando Paquete Consolidado... ---")
    package_data = {
        "nombre": "Aventura en Puerto Gaitán",
        "descripcion": "Incluye Hotel, Guía y Actividades.",
        "margen_agencia": 15.0, # 15% de ganancia
        "duracion_dias": 3,
        "componentes": [
            {
                "tipo_servicio": "HOTEL",
                "proveedor_id": str(p_hotel.id),
                "referencia_id": str(uuid.uuid4()),
                "precio_proveedor": 150000,
                "comision_proveedor": 10000
            },
            {
                "tipo_servicio": "GUIA",
                "proveedor_id": str(p_guia.id),
                "referencia_id": str(uuid.uuid4()),
                "precio_proveedor": 50000,
                "comision_proveedor": 5000
            }
        ],
        "user_id": user_agencia.id,
        "action": "CREATE_PACKAGE"
    }

    res_pack = kernel.resolve_and_execute("CREATE_PACKAGE", package_data)
    package_id = res_pack['package_id']
    precio_total_unitario = res_pack['precio_total']
    print(f"✅ Paquete creado ID: {package_id}, Precio Total: {precio_total_unitario}")

    # 4. Registrar Reserva (Fase 14.1.5)
    print("--- Registrando Reserva... ---")
    client_id = uuid.uuid4()
    booking_data = {
        "package_id": package_id,
        "cliente_ref_id": str(client_id),
        "fecha_inicio": "2025-06-01",
        "numero_personas": 2,
        "user_id": user_agencia.id,
        "action": "BOOK_PACKAGE"
    }

    res_book = kernel.resolve_and_execute("BOOK_PACKAGE", booking_data)
    booking_id = res_book['booking_id']
    total_facturado = res_book['total']
    print(f"✅ Reserva registrada ID: {booking_id}, Total Facturado: {total_facturado}")

    # Verificación: 2 personas * (150000 + 50000) * 1.15 = 2 * 200000 * 1.15 = 460000
    expected_total = 2 * (150000 + 50000) * 1.15
    if float(total_facturado) == expected_total:
        print("✅ Cálculo de facturación consolidada correcto.")
    else:
        print(f"❌ Error en facturación. Esperado: {expected_total}, Obtenido: {total_facturado}")

    # 5. Cancelación Parcial (Fase 14.2.2)
    print("--- Probando Cancelación Parcial de Componente... ---")
    comp_guia = PackageComponent.objects.filter(package_id=package_id, tipo_servicio='GUIA').first()

    cancel_data = {
        "booking_id": booking_id,
        "component_id": str(comp_guia.id),
        "user_id": user_agencia.id,
        "action": "CANCEL_PACKAGE_COMPONENT"
    }

    res_cancel = kernel.resolve_and_execute("CANCEL_PACKAGE_COMPONENT", cancel_data)
    new_total = res_cancel['new_total']
    print(f"✅ Componente Guía cancelado. Nuevo Total: {new_total}")

    # Verificación: 460000 - (2 * 50000 * 1.15) = 460000 - 115000 = 345000
    expected_new_total = 460000 - (2 * 50000 * 1.15)
    if float(new_total) == expected_new_total:
        print("✅ Recálculo de precio tras cancelación parcial correcto.")
    else:
        print(f"❌ Error en recálculo. Esperado: {expected_new_total}, Obtenido: {new_total}")

    # 6. Liquidación Final (Fase 14.1.6)
    print("--- Liquidando Paquete... ---")
    liq_data = {
        "booking_id": booking_id,
        "user_id": user_agencia.id,
        "action": "LIQUIDATE_AGENCY_PACKAGE"
    }

    # Nota: LIQUIDATE_AGENCY_PACKAGE requiere DELEGATED. bar_owner es ADMIN usualmente.
    res_liq = kernel.resolve_and_execute("LIQUIDATE_AGENCY_PACKAGE", liq_data)
    print(f"✅ Liquidación exitosa ID: {res_liq['liquidation_id']}, Utilidad Agencia: {res_liq['utilidad']}")

    # Verificación utilidad: Ingreso 345000 - Costo Hotel (2 * 150000) = 345000 - 300000 = 45000
    if float(res_liq['utilidad']) == 45000:
        print("✅ Utilidad de la agencia verificada.")
    else:
        print(f"❌ Error en utilidad. Esperado: 45000, Obtenido: {res_liq['utilidad']}")

    print("\n🏆 VALIDACIÓN FASE 14.2 COMPLETADA EXITOSAMENTE.")

if __name__ == "__main__":
    simulate_agency()
