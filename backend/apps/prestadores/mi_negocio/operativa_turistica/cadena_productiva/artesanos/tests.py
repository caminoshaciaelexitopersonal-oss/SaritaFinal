from django.test import TestCase
from decimal import Decimal
from api.models import CustomUser
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from .models import RawMaterial, WorkshopOrder, ProductionLog
from .services import ArtisanService

class ArtisanDomainTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="artesano_test", email="art@test.com", password="password")
        self.provider = ProviderProfile.objects.create(
            usuario=self.user,
            nombre_comercial="Taller de Prueba",
            provider_type=ProviderProfile.ProviderTypes.ARTISAN
        )
        self.material = RawMaterial.objects.create(
            provider=self.provider,
            nombre="Arcilla",
            stock_actual=Decimal("10.00"),
            unidad_medida="kg"
        )
        self.order = WorkshopOrder.objects.create(
            provider=self.provider,
            producto_nombre="Jarrón Decorativo",
            fecha_entrega_estimada="2024-12-31"
        )

    def test_production_deduction(self):
        # Registrar producción consume 2kg de arcilla
        log = ArtisanService.registrar_produccion(
            self.order.id,
            self.material.id,
            2,
            "Moldeado inicial"
        )

        self.material.refresh_from_db()
        self.assertEqual(self.material.stock_actual, Decimal("8.00"))
        self.assertEqual(ProductionLog.objects.count(), 1)

    def test_insufficient_stock(self):
        with self.assertRaises(ValueError):
            ArtisanService.registrar_produccion(
                self.order.id,
                self.material.id,
                20,
                "Intento fallido"
            )
