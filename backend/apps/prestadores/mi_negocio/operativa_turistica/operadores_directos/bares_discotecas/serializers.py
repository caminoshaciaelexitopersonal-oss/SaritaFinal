from rest_framework import serializers
from .models import (
    NightclubProfile, NightEvent, NightZone, NightTable,
    NightConsumption, NightConsumptionItem, LiquorInventory,
    InventoryMovement, CashClosing, EventLiquidation
)

class NightclubProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NightclubProfile
        fields = '__all__'

class NightEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = NightEvent
        fields = '__all__'

class NightZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = NightZone
        fields = '__all__'

class NightTableSerializer(serializers.ModelSerializer):
    zona_nombre = serializers.ReadOnlyField(source='zona.nombre')
    class Meta:
        model = NightTable
        fields = '__all__'

class NightConsumptionItemSerializer(serializers.ModelSerializer):
    product_nombre = serializers.ReadOnlyField(source='product.nombre')
    class Meta:
        model = NightConsumptionItem
        fields = '__all__'

class NightConsumptionSerializer(serializers.ModelSerializer):
    items = NightConsumptionItemSerializer(many=True, read_only=True)
    class Meta:
        model = NightConsumption
        fields = '__all__'

class LiquorInventorySerializer(serializers.ModelSerializer):
    product_nombre = serializers.ReadOnlyField(source='product.nombre')
    class Meta:
        model = LiquorInventory
        fields = '__all__'

class InventoryMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryMovement
        fields = '__all__'

class CashClosingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashClosing
        fields = '__all__'

class EventLiquidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLiquidation
        fields = '__all__'
