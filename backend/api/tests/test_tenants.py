import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from api.models import Organization, OrganizationUser, DocumentoVerificacion, TipoDocumentoVerificacion
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

@pytest.mark.django_db
class TenantDataIsolationTests(APITestCase):

    def setUp(self):
        # Crear usuarios
        self.user1 = User.objects.create_user(email='user1@org1.com', password='password123')
        self.user2 = User.objects.create_user(email='user2@org2.com', password='password123')

        # Crear organizaciones
        self.org1 = Organization.objects.create(name='Organización 1', owner=self.user1)
        self.org2 = Organization.objects.create(name='Organización 2', owner=self.user2)

        # Asignar usuarios a organizaciones
        OrganizationUser.objects.create(organization=self.org1, user=self.user1, role='MEMBER')
        OrganizationUser.objects.create(organization=self.org2, user=self.user2, role='MEMBER')

        # Asignar organizacion activa al usuario
        self.user1.organization = self.org1
        self.user1.save()
        self.user2.organization = self.org2
        self.user2.save()

        # Crear un tipo de documento
        self.tipo_doc = TipoDocumentoVerificacion.objects.create(nombre='RUT')

        # Crear documentos, uno para cada organización
        self.doc1 = DocumentoVerificacion.objects.create(
            tipo_documento=self.tipo_doc,
            organization=self.org1
        )
        self.doc2 = DocumentoVerificacion.objects.create(
            tipo_documento=self.tipo_doc,
            organization=self.org2
        )

        # URL del endpoint
        self.url = reverse('documento-verificacion-list')

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_user_can_only_see_documents_from_their_organization(self):
        """
        Verifica que un usuario autenticado solo puede listar los documentos
        pertenecientes a su propia organización.
        """
        token1 = self.get_token(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token1)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], str(self.doc1.id))

    def test_user_cannot_access_documents_from_other_organizations(self):
        """
        Verifica que un usuario no puede acceder directamente a un documento
        de otra organización.
        """
        token1 = self.get_token(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token1)

        url_detalle_doc2 = reverse('documento-verificacion-detail', kwargs={'pk': self.doc2.pk})
        response = self.client.get(url_detalle_doc2)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unauthenticated_user_cannot_access_documents(self):
        """
        Verifica que un usuario no autenticado no puede acceder al endpoint.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
