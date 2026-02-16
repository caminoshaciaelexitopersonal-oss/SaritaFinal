import os
import django
import uuid

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from api.models import CustomUser, Artesano, RubroArtesano
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

def test_artisan_signal():
    print("🧪 PROBANDO SEÑAL DE ACTIVACIÓN AUTOMÁTICA DE ARTESANOS")

    username = f"artesano_{uuid.uuid4().hex[:6]}"
    user = CustomUser.objects.create(username=username, email=f"{username}@test.com", role='TURISTA')

    rubro, _ = RubroArtesano.objects.get_or_create(nombre="Tejidos", slug="tejidos")

    artesano = Artesano.objects.create(
        usuario=user,
        nombre_taller="Taller de Prueba",
        nombre_artesano="Juan Artesano",
        rubro=rubro,
        aprobado=False
    )

    print(f"Usuario inicial rol: {user.role}")
    profile_exists = ProviderProfile.objects.filter(usuario=user).exists()
    print(f"¿Existe ProviderProfile antes de aprobar? {profile_exists}")

    print("Aprobando artesano...")
    artesano.aprobado = True
    artesano.save()

    user.refresh_from_db()
    print(f"Usuario final rol: {user.role}")

    profile = ProviderProfile.objects.filter(usuario=user).first()
    if profile:
        print(f"✅ ProviderProfile CREADO: {profile.nombre_comercial}")
        print(f"✅ Verificado: {profile.is_verified}, Activo: {profile.is_active}")
    else:
        print("❌ FALLO: No se creó el ProviderProfile.")

if __name__ == "__main__":
    test_artisan_signal()
