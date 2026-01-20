
from django.db import transaction
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from api.models import CustomUser
from apps.admin_plataforma.models import Plan, Suscripcion
from decimal import Decimal
from datetime import date, timedelta

class GestionPlataformaService:
    """
    Servicio para manejar la lógica de negocio de la plataforma Sarita
    desde la perspectiva del Administrador General.
    """

    def __init__(self, admin_user: CustomUser):
        if not admin_user.is_staff and not admin_user.is_superuser:
            raise PermissionError("El usuario no tiene permisos de administrador.")
        self.admin_user = admin_user

    def get_sarita_profile(self) -> ProviderProfile:
        """
        Recupera o crea el perfil empresarial para la plataforma Sarita.
        Este perfil se usa para todas las operaciones comerciales propias
        de la plataforma (facturación, contabilidad, etc.).
        """
        # Se asume que existe un usuario específico para la plataforma.
        # Por simplicidad, podríamos usar el propio superusuario admin o un usuario dedicado.
        sarita_user, _ = CustomUser.objects.get_or_create(
            username='sarita_plataforma',
            defaults={
                'email': 'sarita@plataforma.com',
                'role': 'ADMIN',
                'is_staff': True,
            }
        )

        profile, created = ProviderProfile.objects.get_or_create(
            usuario=sarita_user,
            defaults={
                'nombre_negocio': 'Plataforma Sarita',
                'descripcion': 'Perfil empresarial para la gestión de la plataforma Sarita.',
                'email_contacto': 'sarita@plataforma.com',
            }
        )
        return profile

    @transaction.atomic
    def crear_cliente_plataforma(self, nombre_cliente: str, tipo_cliente: str, **kwargs) -> any:
        """
        Crea un nuevo cliente para la Plataforma Sarita.
        Los clientes pueden ser Entes Gubernamentales o Prestadores.

        Ejemplo de uso:
        servicio.crear_cliente_plataforma(
            nombre_cliente="Secretaría de Turismo de Villavicencio",
            tipo_cliente="GUBERNAMENTAL",
            # ... otros campos ...
        )
        """
        # Aquí iría la lógica para crear un nuevo registro de cliente.
        # Por ahora, es un marcador de posición.
        # NOTA: No se debe reutilizar el modelo Cliente de `mi_negocio` directamente
        # si su semántica es diferente. Se podría necesitar un nuevo modelo.

        print(f"Creando cliente '{nombre_cliente}' de tipo '{tipo_cliente}'...")

        # Lógica de creación de cliente (marcador de posición)
        # cliente = PlataformaCliente.objects.create(...)

        return {"status": "success", "message": "Cliente creado (simulado)."}

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

    @transaction.atomic
    def asignar_suscripcion(self, cliente_profile: ProviderProfile, plan: Plan, fecha_inicio: date) -> Suscripcion:
        """Asigna una suscripción de un plan a un cliente."""
        # Lógica para calcular la fecha de fin basada en la frecuencia del plan
        if plan.frecuencia == Plan.Frecuencia.MENSUAL:
            fecha_fin = fecha_inicio + timedelta(days=30)
        elif plan.frecuencia == Plan.Frecuencia.SEMESTRAL:
            fecha_fin = fecha_inicio + timedelta(days=180)
        elif plan.frecuencia == Plan.Frecuencia.ANUAL:
            fecha_fin = fecha_inicio + timedelta(days=365)
        else:
            raise ValueError("Frecuencia de plan no válida.")

        suscripcion = Suscripcion.objects.create(
            cliente=cliente_profile,
            plan=plan,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            is_active=True
        )
        return suscripcion

    # --- Futuros métodos del servicio ---
    # def generar_factura_para_suscripcion(self, suscripcion_id): ...
