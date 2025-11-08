from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404

from .models import Document, DocumentVersion, Process, ProcessType, DocumentType
from .services import DocumentCoordinatorService
from .serializers import (
    DocumentListSerializer, DocumentDetailSerializer, DocumentCreateSerializer,
    DocumentVersionCreateSerializer, DocumentVersionSerializer,
    ProcessTypeSerializer, ProcessSerializer, DocumentTypeSerializer
)

# ==========================================================
# ViewSets para Catálogos (Solo Lectura)
# ==========================================================
class CompanyCatalogViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filtra los catálogos para que solo pertenezcan a la compañía del usuario actual.
        # Se asume que el request.user tiene un perfil con una compañía asociada.
        return self.queryset.filter(company=self.request.user.perfil_prestador.company)

class ProcessTypeViewSet(CompanyCatalogViewSet):
    queryset = ProcessType.objects.all()
    serializer_class = ProcessTypeSerializer

class ProcessViewSet(CompanyCatalogViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        process_type_id = self.request.query_params.get('process_type_id')
        if process_type_id:
            return queryset.filter(process_type_id=process_type_id)
        return queryset

class DocumentTypeViewSet(CompanyCatalogViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer

# ==========================================================
# ViewSet Principal de Documentos
# ==========================================================
class DocumentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        # Solo retorna documentos de la compañía del usuario
        return Document.objects.filter(company=self.request.user.perfil_prestador.company)

    def get_serializer_class(self):
        if self.action == 'list':
            return DocumentListSerializer
        if self.action == 'create':
            return DocumentCreateSerializer
        return DocumentDetailSerializer

    def perform_create(self, serializer):
        # La lógica de creación se mueve al servicio para mantener el ViewSet "delgado"
        file_obj = self.request.data.get('file')
        if not file_obj:
            raise serializers.ValidationError({"file": "Este campo es requerido."})

        validated_data = serializer.validated_data
        validated_data['original_filename'] = file_obj.name
        file_content = file_obj.read()

        DocumentCoordinatorService.create_document_and_first_version(
            data=validated_data,
            user=self.request.user,
            file_content=file_content,
            request=self.request
        )

    @action(detail=True, methods=['post'], url_path='versions')
    def create_version(self, request, pk=None):
        document = self.get_object()
        serializer = DocumentVersionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file_obj = request.data.get('file')
        if not file_obj:
            return Response({"file": ["Este campo es requerido."]}, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data
        validated_data['original_filename'] = file_obj.name
        file_content = file_obj.read()

        new_version = DocumentCoordinatorService.create_new_version_for_document(
            document=document,
            data=validated_data,
            user=request.user,
            file_content=file_content,
            request=request
        )
        response_serializer = DocumentVersionSerializer(new_version)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
