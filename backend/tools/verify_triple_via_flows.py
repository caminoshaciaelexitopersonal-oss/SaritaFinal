import os
import django
import sys

# Setup Django
sys.path.append(os.path.join(os.getcwd(), 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from api.models import CustomUser, GovernmentProfile, Entity
from apps.turismo.models.provider_models import TourismProvider, TourismService, Reservation
from apps.delivery.models import DeliveryService
from django.db import transaction
from django.utils import timezone
from datetime import timedelta

def test_triple_via_flows():
    print("--- INICIANDO PRUEBAS DE FLUJO TRIPLE VÍA ---")

    try:
        # 1. Setup Entities
        nacional_entity, _ = Entity.objects.get_or_create(name="ENTE NACIONAL TEST", slug="ente-nacional-test", type="nacional")
        dept_entity, _ = Entity.objects.get_or_create(name="ENTE DEPT TEST", slug="ente-dept-test", type="departamental")
        mun_entity, _ = Entity.objects.get_or_create(name="ENTE MUN TEST", slug="ente-mun-test", type="municipal")

        # 2. Flow 1: National Director creates National Official
        director_nac, _ = CustomUser.objects.get_or_create(username="director_nac", email="nac@test.com", defaults={"role": CustomUser.Role.DIRECTIVO_NACIONAL})
        director_nac.set_password("password123")
        director_nac.save()

        prof_nac, _ = CustomUser.objects.get_or_create(username="prof_nac", email="prof_nac@test.com", defaults={"role": CustomUser.Role.FUNCIONARIO_PROFESIONAL})
        GovernmentProfile.objects.update_or_create(user=prof_nac, defaults={"entity": nacional_entity, "cargo": "Profesional Nacional", "nivel": "NACIONAL", "created_by": director_nac})
        print("✅ Flujo 1: Director Nacional creó Funcionario Nacional.")

        # 3. Flow 2: Dept Secretary creates Dept Official
        sec_dept, _ = CustomUser.objects.get_or_create(username="sec_dept", email="dept@test.com", defaults={"role": CustomUser.Role.DIRECTIVO_DEPARTAMENTAL})
        prof_dept, _ = CustomUser.objects.get_or_create(username="prof_dept", email="prof_dept@test.com", defaults={"role": CustomUser.Role.FUNCIONARIO_PROFESIONAL})
        GovernmentProfile.objects.update_or_create(user=prof_dept, defaults={"entity": dept_entity, "cargo": "Profesional Departamental", "nivel": "DEPARTAMENTAL", "created_by": sec_dept})
        print("✅ Flujo 2: Secretario Departamental creó Funcionario Departamental.")

        # 4. Flow 3: Mun Secretary creates Mun Official
        sec_mun, _ = CustomUser.objects.get_or_create(username="sec_mun", email="mun@test.com", defaults={"role": CustomUser.Role.DIRECTIVO_MUNICIPAL})
        prof_mun, _ = CustomUser.objects.get_or_create(username="prof_mun", email="prof_mun@test.com", defaults={"role": CustomUser.Role.FUNCIONARIO_PROFESIONAL})
        GovernmentProfile.objects.update_or_create(user=prof_mun, defaults={"entity": mun_entity, "cargo": "Profesional Municipal", "nivel": "MUNICIPAL", "created_by": sec_mun})
        print("✅ Flujo 3: Secretario Municipal creó Funcionario Municipal.")

        # 5. Flow 4: Business Owner creation and Service
        owner, _ = CustomUser.objects.get_or_create(username="owner1", email="owner1@test.com", defaults={"role": CustomUser.Role.BUSINESS_OWNER})
        provider, _ = TourismProvider.objects.get_or_create(name="Hotel Test", owner=owner, defaults={"provider_type": "HOTEL"})
        service, _ = TourismService.objects.get_or_create(provider=provider, name="Suite Real", defaults={"service_type": "ACCOMMODATION", "description": "Lujo llanero", "price": 150000})
        print(f"✅ Flujo 4: Empresa '{provider.name}' y Servicio '{service.name}' creados.")

        # 6. Flow 5: Tourist reservation
        tourist_user, _ = CustomUser.objects.get_or_create(username="turista1", email="turista1@test.com", defaults={"role": CustomUser.Role.TURISTA})
        reserva = Reservation.objects.create(
            provider=provider,
            service=service,
            customer=tourist_user,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=2),
            total_price=300000
        )
        print(f"✅ Flujo 5: Turista '{tourist_user.username}' realizó Reserva ID: {reserva.id}.")

        # 7. Flow 6: Delivery execution (Manual DB insertion)
        delivery_user, _ = CustomUser.objects.get_or_create(username="repartidor1", email="repartidor1@test.com", defaults={"role": CustomUser.Role.DELIVERY_DRIVER})

        import sqlite3
        conn = sqlite3.connect('backend/delivery.sqlite3')
        cur = conn.cursor()
        import uuid
        task_id = uuid.uuid4().hex
        cur.execute("INSERT INTO delivery_deliveryservice (id, tourist_id, origin_address, destination_address, status, estimated_price, created_at, updated_at, comision_repartidor, value_declared, prioridad, tourist_comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (task_id, tourist_user.id, "Restaurante X", "Hotel Test", "ENTREGADO", 5000, timezone.now(), timezone.now(), 0, 0, 'NORMAL', ''))
        conn.commit()
        conn.close()
        print(f"✅ Flujo 6: Delivery '{task_id}' ejecutado (Inserción directa en delivery.sqlite3).")

        # 8. Check Final Counts
        print(f"Total Usuarios: {CustomUser.objects.count()}")
        print(f"Total Perfiles Gob: {GovernmentProfile.objects.count()}")
        print(f"Total Prestadores: {TourismProvider.objects.count()}")
        print(f"Total Reservas: {Reservation.objects.count()}")

        # Verify Delivery
        conn = sqlite3.connect('backend/delivery.sqlite3')
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM delivery_deliveryservice")
        delivery_count = cur.fetchone()[0]
        conn.close()
        print(f"Total Deliveries (delivery.sqlite3): {delivery_count}")

        print("--- PRUEBAS COMPLETADAS CON ÉXITO ---")

    except Exception as e:
        print(f"❌ ERROR EN LAS PRUEBAS: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    test_triple_via_flows()
