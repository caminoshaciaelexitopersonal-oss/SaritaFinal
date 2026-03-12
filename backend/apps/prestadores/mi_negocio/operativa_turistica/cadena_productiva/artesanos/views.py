from rest_framework import viewsets, permissions
from .models import RawMaterial, WorkshopOrder, ProductionLog
from rest_framework import serializers

class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = '__all__'

class WorkshopOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopOrder
        fields = '__all__'

class ProductionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionLog
        fields = '__all__'

class RawMaterialViewSet(viewsets.ModelViewSet):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

class WorkshopOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkshopOrder.objects.all()
    serializer_class = WorkshopOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductionLogViewSet(viewsets.ModelViewSet):
    queryset = ProductionLog.objects.all()
    serializer_class = ProductionLogSerializer
    permission_classes = [permissions.IsAuthenticated]
