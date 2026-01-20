
from django.db import transaction
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from api.models import CustomUser

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

    # --- Futuros métodos del servicio ---
    # def vender_plan_a_cliente(self, cliente_id, plan_id): ...
    # def generar_factura_para_cliente(self, cliente_id, monto): ...
    # def registrar_gasto_operativo(self, descripcion, monto): ...
