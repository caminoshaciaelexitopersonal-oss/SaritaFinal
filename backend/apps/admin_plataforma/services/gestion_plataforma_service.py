
from django.db import transaction
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from api.models import CustomUser
from apps.admin_plataforma.models import Plan, Suscripcion
from decimal import Decimal
from datetime import date, timedelta

class GestionPlataformaService:
    """
    Servicio para manejar la lógica de negocio de la plataforma Sarita
    desde la perspectiva del Administrador General.
    Usa el Dominio Empresarial instanciado para el Super Admin.
    """

    def __init__(self, admin_user: CustomUser):
        if not admin_user.is_staff and not admin_user.is_superuser:
            raise PermissionError("El usuario no tiene permisos de administrador.")
        self.admin_user = admin_user

    @staticmethod
 
    def get_perfil_gobierno_context() -> ProviderProfile:
 
        """
        Retorna el perfil de la organización que actúa como Gobierno/Plataforma
        dentro del dominio administrativo instanciado.
        """
 
        # Obtenemos el usuario administrador (podría haber varios, usamos el primero staff/superuser con email de plataforma o genérico)
        admin_user = CustomUser.objects.filter(is_superuser=True).first()
        if not admin_user:
             admin_user = CustomUser.objects.filter(is_staff=True).first()

        if not admin_user:
            raise ValueError("No se encontró un usuario administrador para el contexto de plataforma.")
 

        profile, created = ProviderProfile.objects.get_or_create(
            usuario=admin_user,
            defaults={
 
                'nombre_negocio': 'Plataforma Sarita (Gobernanza)',
 
            }
        )
        return profile

    @transaction.atomic
    def crear_plan(self, nombre: str, precio: Decimal, frecuencia: str, **kwargs) -> Plan:
        """Crea un nuevo plan de suscripción."""
        plan = Plan.objects.create(
            nombre=nombre,
            precio=precio,
            frecuencia=frecuencia,
            **kwargs
        )
        return plan
