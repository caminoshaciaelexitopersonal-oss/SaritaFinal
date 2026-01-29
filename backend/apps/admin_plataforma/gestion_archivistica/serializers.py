from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_archivistica.models import Document, DocumentVersion, Process, ProcessType, DocumentType

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ['provider']

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'
        read_only_fields = ['provider']
