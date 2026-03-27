import os
import django
import uuid

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from api.models import CustomUser
from apps.social.models import SocialConversation
from rest_framework.test import APIClient
from django.urls import reverse

def verify_protection_flows():
    client = APIClient()

    # Create an unverified user
    username = f"unverified_{uuid.uuid4().hex[:6]}"
    user = CustomUser.objects.create_user(username=username, password="pass", role="TURISTA")
    client.force_authenticate(user=user)

    print(f"\n--- TEST 1: Access Blocked for Unverified User ({username}) ---")
    res = client.get("/api/v1/social/conversations/")
    print(f"Conversations access: {res.status_code}") # Should be 403

    res = client.get("/api/v1/social/protection/status/")
    print(f"Protection status: {res.data['is_protected']}") # Should be False

    print("\n--- TEST 2: Phone Verification Flow ---")
    res = client.post("/api/v1/social/protection/verify-phone/", {"phone": "57311000000", "otp": "123456"})
    print(f"Phone verification: {res.status_code}")

    user.refresh_from_db()
    print(f"User phone_verified: {user.phone_verified}")

    print("\n--- TEST 3: Biometric Face Verification Flow ---")
    # Sending a long string to pass the len > 100 check
    long_image_data = "data:image/jpeg;base64," + "A" * 200
    res = client.post("/api/v1/social/protection/verify-face/", {"image": long_image_data})
    print(f"Face verification: {res.status_code}")

    user.refresh_from_db()
    print(f"User face_verified: {user.face_verified}")
    print(f"Verification status: {user.verification_status}")

    print("\n--- TEST 4: Access Granted for Verified User ---")
    res = client.get("/api/v1/social/conversations/")
    print(f"Conversations access (after verification): {res.status_code}") # Should be 200

if __name__ == "__main__":
    try:
        verify_protection_flows()
    except Exception as e:
        print(f"Test failed: {e}")
        import traceback
        traceback.print_exc()
