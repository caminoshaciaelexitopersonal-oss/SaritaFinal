from rest_framework import serializers
from ..models.provider_models import TourismProvider, BusinessProfile, TourismService, Reservation, TourismSubClassification

class TourismSubClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourismSubClassification
        fields = '__all__'

class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = '__all__'

class TourismProviderSerializer(serializers.ModelSerializer):
    business_profile = BusinessProfileSerializer(read_only=True)
    sub_classification_detail = TourismSubClassificationSerializer(source='sub_classification_ref', read_only=True)
    whatsapp_link = serializers.SerializerMethodField()
    email_link = serializers.SerializerMethodField()
    google_maps_link = serializers.SerializerMethodField()

    class Meta:
        model = TourismProvider
        fields = '__all__'
        read_only_fields = ['owner', 'puntuacion_total']

    def get_whatsapp_link(self, obj):
        phone = obj.contact.get('phone') or obj.contact.get('whatsapp')
        if phone:
            # Clean non-numeric characters
            phone_clean = ''.join(filter(str.isdigit, str(phone)))
            return f"https://wa.me/{phone_clean}"
        return None

    def get_email_link(self, obj):
        email = obj.contact.get('email')
        if email:
            return f"mailto:{email}"
        return None

    def get_google_maps_link(self, obj):
        lat = obj.location.get('lat')
        lng = obj.location.get('lng')
        if lat and lng:
            return f"https://www.google.com/maps/dir/?api=1&destination={lat},{lng}"
        return None

class TourismServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourismService
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
