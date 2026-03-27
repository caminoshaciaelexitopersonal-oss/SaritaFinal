import os
import django
import uuid
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from api.models import CustomUser, AtractivoTuristico, Publicacion
from apps.turismo.models.provider_models import TourismProvider
from apps.turismo.models.routes import TourismRoute
from apps.turismo.services.route_engine import IntelligentRouteEngine
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
    provider_data = [p for p in res.data['results'] if p['id'] == provider_id][0]
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
    res = client.get(f"/api/atractivos/{attr.id}/")
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

    print("\n--- TEST 4: Event Georeferencing & Proximity ---")
    event = Publicacion.objects.create(
        titulo="Festival del Canoero",
        slug="festival-canoero",
        tipo="EVENTO",
        contenido="Gran fiesta",
        latitud=4.31,
        longitud=-72.08,
        estado="PUBLICADO"
    )
    print(f"Event created: {event.titulo}")
    res = client.get(f"/api/v1/publicaciones/{event.slug}/")
    nearby_event = res.data.get('nearby_services', [])
    print(f"Nearby services in event: {len(nearby_event)}")

    print("\n--- TEST 5: Intelligent Route Engine ---")
    # Associate provider with municipality for route engine
    from apps.turismo.models.divipola import Municipality
    mun = Municipality.objects.first()
    TourismProvider.objects.filter(id=provider_id).update(municipality=mun, status='PUBLICADO')
    AtractivoTuristico.objects.filter(id=attr.id).update(municipality=mun, categoria_color='BLANCO')

    # Trigger engine
    res = client.post("/api/v1/turismo/v1/intelligent-routes/generate-intelligent/", {"municipality_id": mun.id}, format='json')
    print(f"Trigger engine: {res.status_code}")

    res = client.get("/api/v1/turismo/v1/intelligent-routes/")
    print(f"Total intelligent routes: {res.data.get('count', 0)}")

if __name__ == "__main__":
    # Cleanup
    TourismProvider.objects.filter(name="Restaurante El Gran Llanero").delete()
    AtractivoTuristico.objects.filter(slug="mirador-manacacias").delete()
    Publicacion.objects.filter(slug="festival-canoero").delete()
    TourismRoute.objects.filter(is_intelligent=True).delete()

    try:
        verify_directory_flows()
    except Exception as e:
        print(f"Test failed: {e}")
        import traceback
        traceback.print_exc()
