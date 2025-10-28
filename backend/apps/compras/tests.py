# backend/apps/compras/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from apps.prestadores.models import Perfil
from apps.contabilidad.models import JournalEntry, ChartOfAccount
from apps.inventario.models import Producto
from .models import Proveedor, FacturaProveedor, PagoRealizado
import datetime

User = get_user_model()

class PagosRealizadosTests(APITestCase):
    def setUp(self):
        # ... (setup completo)
        pass
    def test_registrar_pago_actualiza_factura_y_contabiliza(self):
        # ... (prueba completa)
        pass
