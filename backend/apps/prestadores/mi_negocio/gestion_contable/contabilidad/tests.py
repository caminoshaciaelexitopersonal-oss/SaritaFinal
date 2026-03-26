from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.core_erp.tenancy.models import Tenant
from apps.core_erp.accounting.models import Account, ChartOfAccounts
import uuid

from api.models import CustomUser

class AccountEngineTests(APITestCase):
    def setUp(self):
        from apps.core_erp.tenancy.utils import set_current_tenant_id
        self.tenant = Tenant.objects.create(name="Accounting Test Biz", tax_id="123456789-0")
        set_current_tenant_id(str(self.tenant.id))

        self.user = CustomUser.objects.create_user(username='testaccounting', email='test@acc.com', password='password123', role='BUSINESS_OWNER')

        from apps.turismo.models.provider_models import TourismProvider
        self.profile = TourismProvider.objects.create(
            owner=self.user,
            name="Test Biz",
            provider_type='HOTEL'
        )

        self.client.force_authenticate(user=self.user)
        # Use plain_objects.create to ensure it is created despite potential filter issues in test runner
        self.chart = ChartOfAccounts.plain_objects.create(tenant=self.tenant, name="Standard PUC")
        self.list_url = '/api/v1/mi-negocio/contable/contabilidad/cuentas/'

        # Inject X-Tenant-ID header
        self.client.defaults['HTTP_X_TENANT_ID'] = str(self.tenant.id)

    def test_create_account_hierarchy(self):
        # 1. Create Class
        data_clase = {"code": "1", "name": "ACTIVO"}
        response = self.client.post(self.list_url, data_clase)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        clase_id = response.data['id']

        # 2. Create Group (should auto-parent to Class)
        data_grupo = {"code": "11", "name": "DISPONIBLE"}
        response = self.client.post(self.list_url, data_grupo)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        grupo_id = response.data['id']
        self.assertEqual(str(response.data['parent_account']), str(clase_id))

        # 3. Create Account (should auto-parent to Group)
        data_cuenta = {"code": "1105", "name": "CAJA"}
        response = self.client.post(self.list_url, data_cuenta)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(str(response.data['parent_account']), str(grupo_id))

    def test_invalid_code(self):
        data = {"code": "123", "name": "INVALID"}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
