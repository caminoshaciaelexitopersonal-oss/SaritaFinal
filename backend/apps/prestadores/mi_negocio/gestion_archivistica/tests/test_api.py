# backend/apps/prestadores/mi_negocio/gestion_archivistica/tests/test_api.py
import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

from .factories import UserFactory, DocumentFactory, ProcessFactory, DocumentTypeFactory, CompanyFactory
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil
from apps.prestadores.mi_negocio.gestion_archivistica.models import Document

pytestmark = pytest.mark.django_db

class TestGestionArchivisticaAPI:

    def setup_method(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.company = CompanyFactory()
        self.user.company = self.company
        self.user.save()
        self.perfil = Perfil.objects.create(usuario=self.user, nombre_comercial="Negocio de Prueba", company=self.company)
        self.client.force_authenticate(user=self.user)

    def test_list_documents_returns_only_own_company_docs(self):
        DocumentFactory.create_batch(3, company=self.company)
        other_company = CompanyFactory()
        DocumentFactory.create_batch(2, company=other_company)
        response = self.client.get('/api/v1/mi-negocio/archivistica/documents/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 3
        assert len(response.data['results']) == 3

    def test_retrieve_document_from_other_company_fails(self):
        other_company_doc = DocumentFactory()
        url = f'/api/v1/mi-negocio/archivistica/documents/{other_company_doc.id}/'
        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_create_document_happy_path(self, mocker):
        mock_task = mocker.patch('apps.prestadores.mi_negocio.gestion_archivistica.services.start_file_processing_flow.delay')
        process = ProcessFactory(company=self.company)
        doc_type = DocumentTypeFactory(company=self.company)
        test_file = SimpleUploadedFile("test_report.pdf", b"file content", content_type="application/pdf")
        data = {
            'title': 'New Financial Report',
            'validity_year': 2024,
            'process': process.id,
            'document_type': doc_type.id,
            'file': test_file,
        }
        response = self.client.post('/api/v1/mi-negocio/archivistica/documents/', data=data, format='multipart')
        assert response.status_code == status.HTTP_201_CREATED
        mock_task.assert_called_once()
        assert Document.objects.filter(company=self.company).count() == 1
        new_doc = Document.objects.first()
        assert new_doc.versions.count() == 1
        assert new_doc.versions.first().title == 'New Financial Report'
