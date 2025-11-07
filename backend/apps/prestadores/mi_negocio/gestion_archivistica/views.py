from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import uuid

from .services import DocumentCoordinatorService, db
from .serializers import (
    DocumentListSerializer, DocumentDetailSerializer, DocumentCreateSerializer,
    DocumentVersionCreateSerializer, DocumentVersionSerializer,
    ProcessTypeSerializer, ProcessSerializer, DocumentTypeSerializer
)
from .models import CustomUser # Importamos el dataclass para simular el request.user

# ==========================================================
# Simulación de Autenticación
# ==========================================================
# En un entorno real, `request.user` vendría de Django.
# Para esta implementación sin BD, simulamos un usuario autenticado.
def get_mock_user() -> CustomUser:
    user_id = next(iter(db["users"]))
    return db["users"][user_id]

# ==========================================================
# ViewSets para Catálogos (Solo Lectura)
# ==========================================================
class CompanyCatalogViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated] # Se asume autenticación

    def get_queryset(self):
        user = get_mock_user()
        # Filtra los catálogos para que solo pertenezcan a la compañía del usuario.
        return [item for item in self.queryset if item.company.id == user.company.id]

class ProcessTypeViewSet(CompanyCatalogViewSet):
    queryset = list(db["process_types"].values())
    serializer_class = ProcessTypeSerializer

class ProcessViewSet(CompanyCatalogViewSet):
    queryset = list(db["processes"].values())
    serializer_class = ProcessSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        process_type_id = self.request.query_params.get('process_type_id')
        if process_type_id:
            return [p for p in queryset if p.process_type.id == uuid.UUID(process_type_id)]
        return queryset

class DocumentTypeViewSet(CompanyCatalogViewSet):
    queryset = list(db["document_types"].values())
    serializer_class = DocumentTypeSerializer

# ==========================================================
# ViewSet Principal de Documentos
# ==========================================================
class DocumentViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser] # Para manejar la subida de archivos

    def get_serializer_class(self):
        if self.action == 'list':
            return DocumentListSerializer
        if self.action == 'create':
            return DocumentCreateSerializer
        return DocumentDetailSerializer

    def list(self, request):
        user = get_mock_user()
        # Simula la obtención de documentos para la compañía del usuario
        user_docs = [doc for doc in db["documents"].values() if doc.company.id == user.company.id]

        # Simula la obtención de la última versión para cada documento
        for doc in user_docs:
            versions = [v for v in db["document_versions"].values() if v.document.id == doc.id]
            doc.latest_version = max(versions, key=lambda v: v.version_number, default=None)
            # Para el serializer, necesitamos pasar el objeto proceso completo
            doc.process = db["processes"].get(doc.process.id)

        serializer = DocumentListSerializer(user_docs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_mock_user()
        document = db["documents"].get(uuid.UUID(pk))
        if not document or document.company.id != user.company.id:
            return Response(status=status.HTTP_404_NOT_FOUND)

        document.versions = sorted(
            [v for v in db["document_versions"].values() if v.document.id == document.id],
            key=lambda v: v.version_number, reverse=True
        )
        serializer = DocumentDetailSerializer(document)
        return Response(serializer.data)

    def create(self, request):
        user = get_mock_user()
        serializer = DocumentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file_obj = request.data.get('file')
        if not file_obj:
            return Response({"file": ["Este campo es requerido."]}, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data
        validated_data['original_filename'] = file_obj.name
        file_content = file_obj.read()

        try:
            version = DocumentCoordinatorService.create_document_and_first_version(
                data=validated_data, user=user, file_content=file_content, request=request
            )
            # Para la respuesta, serializamos el documento "padre"
            document = version.document
            document.versions = [version]
            response_serializer = DocumentDetailSerializer(document)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['post'], url_path='versions')
    def create_version(self, request, pk=None):
        user = get_mock_user()
        document = db["documents"].get(uuid.UUID(pk))
        if not document or document.company.id != user.company.id:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DocumentVersionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file_obj = request.data.get('file')
        if not file_obj:
            return Response({"file": ["Este campo es requerido."]}, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data
        validated_data['original_filename'] = file_obj.name
        file_content = file_obj.read()

        new_version = DocumentCoordinatorService.create_new_version_for_document(
            document_id=pk, data=validated_data, user=user, file_content=file_content, request=request
        )
        response_serializer = DocumentVersionSerializer(new_version)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
