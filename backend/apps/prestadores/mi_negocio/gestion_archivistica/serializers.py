from rest_framework import serializers
import uuid

# ==========================================================
# Serializers Anidados (para lectura)
# ==========================================================
# Estos serializers se usan para representar relaciones en las respuestas de la API,
# proporcionando una estructura de datos rica y legible.

class CompanyNestedSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    code = serializers.CharField(read_only=True)

class UserNestedSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    username = serializers.CharField(read_only=True)

class ProcessNestedSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    code = serializers.CharField(read_only=True)

class DocumentTypeNestedSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    code = serializers.CharField(read_only=True)

# ==========================================================
# Serializers de Versiones de Documento
# ==========================================================

class DocumentVersionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    version_number = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    uploaded_at = serializers.DateTimeField(read_only=True)
    uploaded_by = UserNestedSerializer(read_only=True)
    status = serializers.CharField(read_only=True)
    file_hash_sha256 = serializers.CharField(read_only=True, required=False)
    blockchain_transaction = serializers.CharField(read_only=True, required=False)
    blockchain_timestamp = serializers.DateTimeField(read_only=True, required=False)

class DocumentVersionCreateSerializer(serializers.Serializer):
    title = serializers.CharField(write_only=True)
    validity_year = serializers.IntegerField(write_only=True)
    # El campo 'file' se manejará directamente en la vista.

# ==========================================================
# Serializers de Documentos (Contenedores)
# ==========================================================

class DocumentListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    document_code = serializers.CharField(read_only=True)
    process = ProcessNestedSerializer(source="*", read_only=True) # Fuente es el objeto doc
    latest_version = DocumentVersionSerializer(read_only=True)

class DocumentDetailSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    document_code = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    process = ProcessNestedSerializer(read_only=True)
    document_type = DocumentTypeNestedSerializer(read_only=True)
    created_by = UserNestedSerializer(read_only=True)
    versions = DocumentVersionSerializer(many=True, read_only=True)

class DocumentCreateSerializer(serializers.Serializer):
    title = serializers.CharField(write_only=True, max_length=200)
    validity_year = serializers.IntegerField(write_only=True)
    process_id = serializers.UUIDField(write_only=True)
    document_type_id = serializers.UUIDField(write_only=True)
    # El campo 'file' se manejará en la vista.

# ==========================================================
# Serializers de Catálogos (Solo Lectura)
# ==========================================================

class ProcessTypeSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    code = serializers.CharField(read_only=True)

class ProcessSerializer(ProcessNestedSerializer):
    pass # Hereda de la versión anidada ya que los campos son los mismos

class DocumentTypeSerializer(DocumentTypeNestedSerializer):
    pass # Hereda de la versión anidada
