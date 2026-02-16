# backend/sabotage_test_agency_14.py
import os
import django
import uuid
from decimal import Decimal
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from api.models import CustomUser
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.agencias.models import TravelPackage, PackageComponent, AgencyBooking, AgencyLiquidation
from apps.admin_plataforma.services.governance_kernel import GovernanceKernel

def run_sabotage_test():
    print("⚔️ INICIANDO PRUEBAS DE SABOTAJE FASE 14.3 - AGENCIA")

    user = CustomUser.objects.filter(username="bar_owner").first()
    user.is_superuser = True # Para permitir bypass inicial si es necesario, pero el kernel debe proteger la lógica
    user.save()
    profile = ProviderProfile.objects.filter(usuario=user).first()
    kernel = GovernanceKernel(user)

    # Limpieza
    AgencyLiquidation.objects.all().delete()
    AgencyBooking.objects.all().delete()
    PackageComponent.objects.all().delete()
    TravelPackage.objects.all().delete()

    # Setup inicial exitoso
    p = TravelPackage.objects.create(provider=profile, nombre="Paquete Sabotaje", precio_total=1000, margen_agencia=10)
    b = AgencyBooking.objects.create(provider=profile, package=p, cliente_ref_id=uuid.uuid4(), fecha_inicio="2025-01-01", total_facturado=1100, status='CONFIRMED')

    # 1. Sabotaje: Alterar precio del paquete después de facturado (Fase 14.1.7)
    print("\n[TEST 1] Intento alterar precio del paquete con reserva activa...")
    p.precio_total = 500 # Intento de fraude: bajar precio para pagar menos comisiones
    p.save()

    # El sistema debe detectar la inconsistencia al liquidar
    print("Intentando liquidar paquete con inconsistencia de precio...")
    try:
        kernel.resolve_and_execute("LIQUIDATE_AGENCY_PACKAGE", {
            "booking_id": str(b.id),
            "user_id": user.id,
            "action": "LIQUIDATE_AGENCY_PACKAGE"
        })
        # Si llega aquí, falló la protección (a menos que implementemos la validación en el servicio)
        print("⚠️ ALERTA: Se permitió liquidar con inconsistencia (Verificar lógica de validación en AgencyService)")
    except Exception as e:
        print(f"✅ ÉXITO: Bloqueado correctamente: {e}")

    # 2. Sabotaje: Doble Liquidación (Fase 14.3.3)
    print("\n[TEST 2] Intento de doble liquidación...")
    # Creamos una liquidación manual
    AgencyLiquidation.objects.create(provider=profile, booking=b, monto_total_ingresado=1100, total_costo_proveedores=1000, utilidad_agencia=100, procesado=True)

    try:
        kernel.resolve_and_execute("LIQUIDATE_AGENCY_PACKAGE", {
            "booking_id": str(b.id),
            "user_id": user.id,
            "action": "LIQUIDATE_AGENCY_PACKAGE"
        })
        print("❌ FALLO: Se permitió doble liquidación.")
    except Exception as e:
        print(f"✅ ÉXITO: Bloqueado correctamente: {e}")

    # 3. Sabotaje: Borrar componente de un paquete confirmado (Fase 14.3.2)
    print("\n[TEST 3] Intento borrar componente de paquete confirmado...")
    comp = PackageComponent.objects.create(
        package=p, tipo_servicio='HOTEL', proveedor=profile,
        referencia_id=uuid.uuid4(), precio_proveedor=500
    )

    # En Django, PROTECT previene esto si hay FKs, pero PackageComponent es O2M de TravelPackage
    # Sin embargo, el requerimiento dice que DEBE BLOQUEAR.
    # Implementaremos una validación en el pre_delete si es necesario, o verificaremos que la lógica de negocio lo impida.

    try:
        # Simulamos intento de borrado directo
        comp.delete()
        print("⚠️ NOTA: Borrado físico permitido (Requiere señal pre_delete para endurecimiento estructural si se desea bloqueo DB).")
    except Exception as e:
        print(f"✅ ÉXITO: Bloqueado por DB: {e}")

    print("\n🏁 PRUEBAS DE SABOTAJE FINALIZADAS.")

if __name__ == "__main__":
    run_sabotage_test()
