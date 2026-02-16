# backend/simulate_artisan_15.py
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
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product
from apps.prestadores.mi_negocio.operativa_turistica.cadena_productiva.artesanos.models import RawMaterial, ArtisanProduct, WorkshopOrder
from apps.admin_plataforma.services.governance_kernel import GovernanceKernel

def simulate_artisan():
    print("🚀 INICIANDO SIMULACIÓN DE TALLER ARTESANAL FASE 15.2")

    # 0. Limpieza
    WorkshopOrder.objects.all().delete()
    RawMaterial.objects.all().delete()
    ArtisanProduct.objects.all().delete()

    # 1. Setup - Usuario Artesano
    user_artesano, _ = CustomUser.objects.get_or_create(
        username="artisan_master",
        defaults={"role":"ARTESANO", "email":"artisan@test.com", "is_superuser": True}
    )
    # Re-asegurar rol y permisos
    user_artesano.role = "ARTESANO"
    user_artesano.is_superuser = True
    user_artesano.save()

    profile_artesano, _ = ProviderProfile.objects.get_or_create(
        usuario=user_artesano,
        defaults={"nombre_comercial": "Taller del Sol", "provider_type":"ARTISAN"}
    )
    kernel = GovernanceKernel(user_artesano)

    # 2. Registrar Materia Prima
    print("--- Registrando Materia Prima... ---")
    res_mat = kernel.resolve_and_execute("REGISTER_RAW_MATERIAL", {
        "nombre": "Barro Rojo",
        "unidad_medida": "Kg",
        "cantidad": 50,
        "costo_por_unidad": 5000,
        "user_id": user_artesano.id,
        "action": "REGISTER_RAW_MATERIAL"
    })
    material_id = res_mat['material_id']
    print(f"✅ Materia Prima registrada: {res_mat['stock']} Kg")

    # 3. Crear Producto Artesanal
    print("--- Configurando Producto Artesanal... ---")
    generic_product = Product.objects.create(provider=profile_artesano, nombre="Jarrón Ancestral", base_price=120000)
    art_product = ArtisanProduct.objects.create(
        product=generic_product,
        tecnica_usada="Torneado manual",
        es_por_encargo=True
    )

    # 4. Iniciar Orden de Taller
    print("--- Iniciando Pedido Personalizado... ---")
    client_id = uuid.uuid4()
    res_order = kernel.resolve_and_execute("CREATE_WORKSHOP_ORDER", {
        "cliente_ref_id": str(client_id),
        "artisan_product_id": str(art_product.id),
        "especificaciones": "Grabado con motivos de palma real.",
        "fecha_entrega_prometida": "2025-07-15",
        "total_precio": 150000,
        "anticipo_pagado": 50000,
        "user_id": user_artesano.id,
        "action": "CREATE_WORKSHOP_ORDER"
    })
    order_id = res_order['order_id']
    print(f"✅ Orden de taller creada ID: {order_id}")

    # 5. Avanzar Producción con Consumo de Material
    print("--- Avanzando Producción (Consumo de Material)... ---")
    res_stage = kernel.resolve_and_execute("UPDATE_PRODUCTION_STAGE", {
        "order_id": order_id,
        "nueva_etapa": "PRODUCCION",
        "descripcion": "Iniciando moldeado de la pieza.",
        "materiales": [
            {"material_id": material_id, "cantidad": 5}
        ],
        "user_id": user_artesano.id,
        "action": "UPDATE_PRODUCTION_STAGE"
    })
    print(f"✅ Producción avanzada a: {res_stage['estado']}")

    # Verificación de Stock
    mat_final = RawMaterial.objects.get(id=material_id)
    print(f"📊 Stock final de Barro: {mat_final.stock_actual} Kg (Esperado: 45.0)")

    if mat_final.stock_actual == Decimal('45.00'):
        print("\n🏆 VALIDACIÓN FASE 15.2 EXITOSA: Taller operativo al 100%.")

if __name__ == "__main__":
    simulate_artisan()
