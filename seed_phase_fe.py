import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from api.models import CustomUser

# Create SuperAdmin if not exists
if not CustomUser.objects.filter(email="superadmin@sarita.com").exists():
    CustomUser.objects.create_superuser(
        email="superadmin@sarita.com",
        username="superadmin",
        password="admin123",
        role="ADMIN"
    )
    print("SuperAdmin created.")
else:
    u = CustomUser.objects.get(email="superadmin@sarita.com")
    u.set_password("admin123")
    u.save()
    print("SuperAdmin password reset.")
