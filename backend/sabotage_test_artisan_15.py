# backend/sabotage_test_artisan_15.py
import os
import django
import uuid
from decimal import Decimal
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from api.models import CustomUser
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product
from apps.prestadores.mi_negocio.operativa_turistica.cadena_productiva.artesanos.models import RawMaterial, ArtisanProduct, WorkshopOrder
from apps.admin_plataforma.services.governance_kernel import GovernanceKernel

def run_sabotage_test():
    print("⚔️ INICIANDO PRUEBAS DE SABOTAJE FASE 15.3 - ARTESANOS")

    user = CustomUser.objects.filter(username="artisan_master").first()
    profile = ProviderProfile.objects.filter(usuario=user).first()
    kernel = GovernanceKernel(user)

    # 1. Sabotaje: Consumo de material inexistente
    print("\n[TEST 1] Intento consumir material que no existe...")
    try:
        kernel.resolve_and_execute("UPDATE_PRODUCTION_STAGE", {
            "order_id": str(uuid.uuid4()), # Fake order
            "nueva_etapa": "PRODUCCION",
            "materiales": [{"material_id": str(uuid.uuid4()), "cantidad": 10}],
            "user_id": user.id,
            "action": "UPDATE_PRODUCTION_STAGE"
        })
        print("❌ FALLO: Se permitió actualizar con datos fake.")
    except Exception as e:
        print(f"✅ ÉXITO: Bloqueado correctamente: {e}")

    # 2. Sabotaje: Agotar stock intencionalmente
    print("\n[TEST 2] Intento consumir más material del disponible...")
    mat = RawMaterial.objects.create(provider=profile, nombre="Lana", stock_actual=10, unidad_medida="m")
    prod = Product.objects.create(provider=profile, nombre="Ruana", base_price=50000)
    art_prod = ArtisanProduct.objects.create(product=prod, tecnica_usada="Tejido")
    order = WorkshopOrder.objects.create(provider=profile, cliente_ref_id=uuid.uuid4(), artisan_product=art_prod, fecha_entrega_prometida="2025-01-01", total_precio=60000)

    try:
        kernel.resolve_and_execute("UPDATE_PRODUCTION_STAGE", {
            "order_id": str(order.id),
            "nueva_etapa": "PRODUCCION",
            "materiales": [{"material_id": str(mat.id), "cantidad": 100}], # Excede stock (10)
            "user_id": user.id,
            "action": "UPDATE_PRODUCTION_STAGE"
        })
        print("❌ FALLO: Se permitió sobreconsumo de material.")
    except Exception as e:
        print(f"✅ ÉXITO: Bloqueado correctamente: {e}")

    # 3. Sabotaje: Violación de Autoridad (Turista intentando registrar materia prima)
    print("\n[TEST 3] Turista intentando registrar materia prima...")
    turista, _ = CustomUser.objects.get_or_create(username="turista_hacker", defaults={"role":"TURISTA"})
    kernel_hacker = GovernanceKernel(turista)

    try:
        kernel_hacker.resolve_and_execute("REGISTER_RAW_MATERIAL", {
            "nombre": "Oro Falso",
            "unidad_medida": "g",
            "cantidad": 1000,
            "costo_por_unidad": 1,
            "user_id": turista.id,
            "action": "REGISTER_RAW_MATERIAL"
        })
        print("❌ FALLO: Turista pudo registrar suministros.")
    except Exception as e:
        print(f"✅ ÉXITO: Bloqueado por el Kernel de Gobernanza: {e}")

    print("\n🏁 PRUEBAS DE SABOTAJE FINALIZADAS.")

if __name__ == "__main__":
    run_sabotage_test()
