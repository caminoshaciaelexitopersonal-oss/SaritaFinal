import os
import django
import uuid
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from api.models import CustomUser, AtractivoTuristico, Entity
from apps.turismo.models.provider_models import TourismProvider
from rest_framework.test import APIClient
from django.urls import reverse

def verify_directory_flows():
    client = APIClient()
    admin = CustomUser.objects.get(username="admin_test")
    client.force_authenticate(user=admin)

    print("\n--- TEST 1: Provider Registration & Approval ---")
    # 1. Create a provider
    res = client.post("/api/v1/turismo/v1/tourism-providers/", {
        "name": "Restaurante El Gran Llanero",
        "provider_type": "RESTAURANT",
        "location": {"address": "Calle Principal 123", "lat": 4.31, "lng": -72.08},
        "contact": {"phone": "573112223344", "email": "contacto@llanero.co"},
        "status": "PENDIENTE"
    }, format='json')
    print(f"Provider creation: {res.status_code}")
    provider_id = res.data['id']

    # 2. Check visibility (should not be in public list yet)
    res = client.get("/api/v1/turismo/v1/tourism-providers/")
    print(f"Public list count (before approval): {res.data.get('count', 0)}")

    # 3. Institutional Approval
    res = client.post(f"/api/v1/turismo/v1/tourism-providers/{provider_id}/approve/")
    print(f"Institutional approval: {res.status_code}")

    # 4. Check visibility (should be in public list now)
    res = client.get("/api/v1/turismo/v1/tourism-providers/")
    print(f"Public list count (after approval): {res.data.get('count', 0)}")

    # 5. Verify Contact Links
    provider_data = res.data['results'][0]
    print(f"WhatsApp Link: {provider_data.get('whatsapp_link')}")
    print(f"Google Maps Link: {provider_data.get('google_maps_link')}")

    print("\n--- TEST 2: Attraction Proximity ---")
    # 1. Create an attraction near the provider
    attr = AtractivoTuristico.objects.create(
        nombre="Mirador del Río Manacacías",
        slug="mirador-manacacias",
        descripcion="Vista espectacular",
        latitud=4.312,
        longitud=-72.081,
        categoria_color="AMARILLO",
        es_publicado=True
    )
    print(f"Attraction created: {attr.nombre}")

    # 2. Retrieve attraction details and check nearby services
    # AtractivoTuristicoViewSet in api/urls.py is included at /api/
    # It uses integer PKs (default for this model)
    res = client.get(f"/api/atractivos/{attr.id}/")

    if res.status_code != 200:
         print(f"Failed to get attraction detail at /api/atractivos/{attr.id}/. Status: {res.status_code}")
         # Try by slug
         res = client.get(f"/api/atractivos/{attr.slug}/")
         if res.status_code != 200:
             print(f"Failed to get attraction detail by slug. Status: {res.status_code}")
             nearby = []
         else:
             nearby = res.data.get('nearby_services', [])
    else:
         nearby = res.data.get('nearby_services', [])
    print(f"Nearby services count: {len(nearby)}")
    if len(nearby) > 0:
        print(f"First nearby service: {nearby[0]['name']} ({nearby[0]['provider_type']})")

    print("\n--- TEST 3: Nearby Search API ---")
    # 1. Test the 'nearby' action directly
    res = client.get(f"/api/v1/turismo/v1/tourism-providers/nearby/?lat=4.31&lng=-72.08&radius=5")
    print(f"Nearby API count: {len(res.data)}")
    if len(res.data) > 0:
        print(f"Found: {res.data[0]['name']}")

if __name__ == "__main__":
    # Cleanup
    TourismProvider.objects.filter(name="Restaurante El Gran Llanero").delete()
    AtractivoTuristico.objects.filter(slug="mirador-manacacias").delete()

    try:
        verify_directory_flows()
    except Exception as e:
        print(f"Test failed: {e}")
