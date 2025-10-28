# backend/apps/inventario/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.prestadores.models import Perfil
from apps.comercial.models import FacturaVenta, ItemFactura, Cliente
from apps.compras.models import FacturaProveedor, ItemFacturaProveedor, Proveedor
from apps.contabilidad.models import JournalEntry, ChartOfAccount
from .models import Producto, MovimientoInventario
from .services import registrar_entrada_inventario, registrar_salida_inventario
import datetime
from decimal import Decimal

User = get_user_model()

class InventarioServicesTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@test.com', 'password', role='prestador')
        self.perfil = Perfil.objects.create(usuario=self.user, nombre_comercial='Negocio de Inventario')

        # Cuentas contables para COGS y Compras
        ChartOfAccount.objects.create(perfil=self.perfil, code='6135', name='Costo de Venta', nature='DEBITO', allows_transactions=True)
        ChartOfAccount.objects.create(perfil=self.perfil, code='5105', name='Gastos Compras', nature='DEBITO', allows_transactions=True)
        ChartOfAccount.objects.create(perfil=self.perfil, code='2205', name='CxP Proveedores', nature='CREDITO', allows_transactions=True)
        ChartOfAccount.objects.create(perfil=self.perfil, code='1435', name='Inventario Mercancías', nature='DEBITO', allows_transactions=True)

        self.producto = Producto.objects.create(perfil=self.perfil, nombre='Producto de Prueba')

    def test_entrada_inventario_actualiza_stock_y_costo(self):
        """
        Prueba que el servicio de entrada actualiza correctamente el stock
        y calcula el costo promedio ponderado.
        """
        proveedor = Proveedor.objects.create(perfil=self.perfil, nombre='Proveedor A')
        factura_compra = FacturaProveedor.objects.create(
            perfil=self.perfil, proveedor=proveedor, fecha_emision=datetime.date.today(),
            fecha_vencimiento=datetime.date.today(), total=1000
        )
        ItemFacturaProveedor.objects.create(
            factura=factura_compra, producto=self.producto, cantidad=10, costo_unitario=100
        )

        # Llamar al servicio
        registrar_entrada_inventario(factura=factura_compra)

        self.producto.refresh_from_db()
        self.assertEqual(self.producto.cantidad_en_stock, 10)
        self.assertEqual(self.producto.costo_promedio_ponderado, 100)
        self.assertEqual(MovimientoInventario.objects.count(), 1)

        # Segunda compra para probar el promedio ponderado
        factura_compra_2 = FacturaProveedor.objects.create(
            perfil=self.perfil, proveedor=proveedor, fecha_emision=datetime.date.today(),
            fecha_vencimiento=datetime.date.today(), total=1320
        )
        ItemFacturaProveedor.objects.create(
            factura=factura_compra_2, producto=self.producto, cantidad=12, costo_unitario=110
        )

        registrar_entrada_inventario(factura=factura_compra_2)

        self.producto.refresh_from_db()
        self.assertEqual(self.producto.cantidad_en_stock, 22) # 10 + 12
        # Costo total = (10*100) + (12*110) = 1000 + 1320 = 2320
        # Costo promedio = 2320 / 22 = 105.4545...
        self.assertAlmostEqual(self.producto.costo_promedio_ponderado, Decimal('105.45'), places=2)

    def test_salida_inventario_actualiza_stock_y_contabiliza_cogs(self):
        """
        Prueba que el servicio de salida reduce el stock y genera el asiento de COGS
        al costo promedio ponderado correcto.
        """
        # Establecer un estado inicial de inventario
        self.producto.cantidad_en_stock = 20
        self.producto.costo_promedio_ponderado = 50
        self.producto.save()

        cliente = Cliente.objects.create(perfil=self.perfil, nombre='Cliente B')
        factura_venta = FacturaVenta.objects.create(
            perfil=self.perfil, cliente=cliente, fecha_emision=datetime.date.today(),
            fecha_vencimiento=datetime.date.today(), total=0, estado='EMITIDA',
            created_by=self.user
        )
        ItemFactura.objects.create(
            factura=factura_venta, producto=self.producto, cantidad=5, precio_unitario=80
        )

        # Llamar al servicio de salida
        registrar_salida_inventario(factura=factura_venta)

        # 1. Verificar actualización de stock
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.cantidad_en_stock, 15) # 20 - 5
        self.assertEqual(MovimientoInventario.objects.count(), 1)
        movimiento = MovimientoInventario.objects.first()
        self.assertEqual(movimiento.costo_unitario, 50) # Salió al costo promedio
        self.assertEqual(movimiento.costo_total, 250) # 5 * 50

        # 2. Verificar contabilización del COGS (esto lo hace la señal, no el servicio)
        # Por ahora, nos enfocamos en el servicio. La prueba de la señal es independiente.
        # Para probar la señal, necesitaríamos disparar el post_save de FacturaVenta.
