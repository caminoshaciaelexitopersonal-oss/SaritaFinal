import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from apps.turismo.models.provider_models import TourismProvider, TourismSubClassification
from api.models import CustomUser
from rest_framework.test import APIClient
from django.urls import reverse

def verify_rnt_login_and_subclassification():
    client = APIClient()

    # 1. Setup Data
    user, _ = CustomUser.objects.get_or_create(username="rnt_owner", defaults={"role": "BUSINESS_OWNER"})
    user.set_password("pass123")
    user.save()

    sub = TourismSubClassification.objects.get(slug="hotel-hotel-boutique")

    provider, _ = TourismProvider.objects.update_or_create(
        rnt_number="RNT-12345",
        defaults={
            "name": "Boutique Hotel Test",
            "provider_type": "HOTEL",
            "owner": user,
            "sub_classification_ref": sub
        }
    )

    print(f"Created Provider: {provider.name} with RNT: {provider.rnt_number}")

    # 2. Test RNT Login Action
    # The URL in the project is /api/v1/turismo/v1/tourism-providers/login-rnt/
    url = "/api/v1/turismo/v1/tourism-providers/login-rnt/"
    response = client.post(url, {"rnt_number": "RNT-12345"}, format='json')

    print(f"Login RNT Status: {response.status_code}")
    if response.status_code == 200:
        print(f"Login RNT Response: {response.data}")
        print("SUCCESS: RNT Login verified.")
    else:
        print(f"FAILED: RNT Login failed. Status: {response.status_code}")

    # 3. Test Sub-classification API
    url_sub = "/api/v1/turismo/v1/sub-classifications/"
    res_sub = client.get(url_sub, {"category": "HOTEL"}, format='json')
    print(f"Sub-classifications count (HOTEL): {res_sub.data.get('count')}")

    if res_sub.data.get('count') >= 50:
        print("SUCCESS: Sub-classification seeding verified.")
    else:
        print(f"FAILED: Sub-classification count is {res_sub.data.get('count')}, expected >= 50.")

if __name__ == "__main__":
    verify_rnt_login_and_subclassification()
