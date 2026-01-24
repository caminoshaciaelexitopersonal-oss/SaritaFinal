import os
import django
from django.conf import settings
from django.test.utils import setup_test_environment

# Configurar el entorno de prueba de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')

# Configurar una base de datos en memoria para la prueba
settings.DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory:',
}

django.setup()
setup_test_environment()

from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory
from api.serializers import CustomUserDetailSerializer
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

User = get_user_model()

def run_test():
    """
    Ejecuta la prueba de verificación del serializador de usuario.
    """
    print("--- Iniciando prueba de verificación de la reparación de autenticación ---")

    # 1. Crear un usuario PRESTADOR sin perfil asociado
    # Esto simula un usuario recién registrado.
    test_user_email = 'testprestador@example.com'
    test_user_password = 'password123'

    # Limpiar cualquier usuario de pruebas anteriores
    User.objects.filter(email=test_user_email).delete()

    user = User.objects.create_user(
        username=test_user_email,
        email=test_user_email,
        password=test_user_password,
        role='PRESTADOR'
    )
    print(f"Paso 1: Creado usuario de prueba '{user.email}' con rol '{user.role}'.")

    # 2. Intentar serializar el usuario usando el serializador reparado
    # Se simula una 'request' de API, que es necesaria para el contexto del serializador.
    factory = APIRequestFactory()
    request = factory.get('/api/auth/user/')

    print("Paso 2: Intentando serializar el usuario con CustomUserDetailSerializer...")
    try:
        serializer = CustomUserDetailSerializer(instance=user, context={'request': request})
        data = serializer.data
        print("   -> Serialización completada con éxito.")
    except Exception as e:
        print(f"   [FALLO] La serialización falló con una excepción: {e}")
        return

    # 3. Verificar que la serialización fue exitosa y los campos son correctos
    print("Paso 3: Verificando el contenido del resultado serializado...")

    # Verificar que el serializador no falló
    assert data is not None, "[FALLO] El resultado de la serialización es None."

    # Verificar que los campos principales existen
    assert 'pk' in data, "[FALLO] 'pk' no está en el resultado."
    assert 'email' in data, "[FALLO] 'email' no está en el resultado."
    assert 'role' in data, "[FALLO] 'role' no está en el resultado."

    # La verificación más importante: el perfil_prestador debe ser None y no causar un error.
    assert 'perfil_prestador' in data, "[FALLO] 'perfil_prestador' no está en el resultado."
    if data['perfil_prestador'] is None:
        print("   -> [ÉXITO] El campo 'perfil_prestador' es None, como se esperaba para un usuario sin perfil.")
    else:
        print(f"   [FALLO] El campo 'perfil_prestador' no es None. Contiene: {data['perfil_prestador']}")
        return

    print("\n--- Prueba de verificación completada con ÉXITO. ---")
    print("El serializador ahora maneja de forma segura a los usuarios sin perfiles asociados.")
    print("La causa raíz del fallo de autenticación en el backend ha sido resuelta.")

    # Limpieza final
    user.delete()
    print("\nUsuario de prueba eliminado.")


if __name__ == '__main__':
    run_test()
