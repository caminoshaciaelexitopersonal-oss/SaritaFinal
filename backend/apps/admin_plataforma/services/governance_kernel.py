import logging
from typing import Dict, Any, Optional
from django.db import transaction
from api.models import CustomUser
from apps.admin_plataforma.models import GovernanceAuditLog

logger = logging.getLogger(__name__)

class GovernanceIntention:
    """
    Representa una intención abstracta de negocio con su contrato.
    """
    def __init__(self, name: str, domain: str, required_role: str, required_params: list = None):
        self.name = name
        self.domain = domain
        self.required_role = required_role
        self.required_params = required_params or []

class GovernanceKernel:
    """
    El Núcleo de Gobernanza Central de Sarita.
    Responsable de validar autoridad, resolver intenciones y coordinar flujos.
    """

    _registry: Dict[str, GovernanceIntention] = {}

    @classmethod
    def register_intention(cls, intention: GovernanceIntention):
        cls._registry[intention.name] = intention
        logger.info(f"KERNEL: Intención '{intention.name}' registrada en el dominio '{intention.domain}'.")

    def __init__(self, user: CustomUser):
        self.user = user

    def resolve_and_execute(self, intention_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Punto de entrada único para ejecutar intenciones.
        """
        logger.info(f"KERNEL: Recibida intención '{intention_name}' de usuario {self.user.username}")

        # 1. Resolver intención
        intention = self._registry.get(intention_name)
        if not intention:
            raise ValueError(f"Intención '{intention_name}' no reconocida por el núcleo de gobernanza.")

        # 2. Validar Contrato (Requisitos de parámetros)
        self._validate_contract(intention, parameters)

        # 3. Validar Autoridad
        self._validate_authority(intention)

        # 4. Coordinar y Ejecutar
        try:
            with transaction.atomic():
                result = self._dispatch(intention, parameters)

                # 4. Auditoría Sistémica Unificada
                self._log_audit(intention, parameters, result)

                return result
        except Exception as e:
            logger.error(f"KERNEL: Error ejecutando '{intention_name}': {str(e)}")
            self._log_audit(intention, parameters, {}, success=False, error_message=str(e))
            raise e

    def _validate_contract(self, intention: GovernanceIntention, parameters: Dict[str, Any]):
        """
        Valida que los parámetros cumplan con el contrato de la intención.
        """
        missing = [p for p in intention.required_params if p not in parameters]
        if missing:
            raise ValueError(f"Contrato violado para '{intention.name}': Faltan parámetros requeridos: {missing}")

    def _validate_authority(self, intention: GovernanceIntention):
        """
        Verifica si el usuario tiene permiso para ejecutar la intención.
        """
        # Regla de oro: SuperAdmin tiene acceso a todo en gobernanza.
        if self.user.is_superuser:
            return True

        if self.user.role != intention.required_role:
             raise PermissionError(f"El usuario no tiene el rol '{intention.required_role}' requerido para '{intention.name}'.")

        return True

    def _dispatch(self, intention: GovernanceIntention, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la ejecución al servicio de dominio correspondiente.
        """
        from .gestion_plataforma_service import GestionPlataformaService
        service = GestionPlataformaService(admin_user=self.user)

        if intention.name == "PLATFORM_CREATE_PLAN":
            plan = service.crear_plan(
                nombre=parameters["nombre"],
                precio=parameters["precio"],
                frecuencia=parameters["frecuencia"],
                descripcion=parameters.get("descripcion", "")
            )
            return {"status": "SUCCESS", "id": plan.id, "message": f"Plan '{plan.nombre}' creado."}

        # Futuras intenciones se mapean aquí
        return {"status": "SUCCESS", "message": f"Intención '{intention.name}' procesada correctamente."}

    def _log_audit(self, intention: GovernanceIntention, parameters: Dict[str, Any], result: Dict[str, Any], success: bool = True, error_message: str = None):
        """
        Registra la acción en el log de auditoría sistémica.
        """
        try:
             GovernanceAuditLog.objects.create(
                 usuario=self.user,
                 intencion=intention.name,
                 parametros=parameters,
                 resultado=result,
                 success=success,
                 error_message=error_message
             )
             logger.info(f"AUDIT KERNEL: Usuario={self.user.username}, Acción={intention.name}")
        except Exception as e:
            logger.error(f"Error al registrar auditoría en el Kernel: {e}")

# --- REGISTRO DE INTENCIONES INICIALES (Fase 3.5) ---

# Dominio: Plataforma
GovernanceKernel.register_intention(GovernanceIntention(
    name="PLATFORM_CREATE_PLAN",
    domain="plataforma",
    required_role=CustomUser.Role.ADMIN,
    required_params=["nombre", "precio", "frecuencia"]
))

GovernanceKernel.register_intention(GovernanceIntention(
    name="PLATFORM_SUSPEND_USER",
    domain="plataforma",
    required_role=CustomUser.Role.ADMIN,
    required_params=["user_id", "motivo"]
))

# Dominio: ERP Sistémico (Comercial)
GovernanceKernel.register_intention(GovernanceIntention(
    name="ERP_CONFIRM_SALE",
    domain="comercial",
    required_role=CustomUser.Role.ADMIN,
    required_params=["operacion_id"]
))

# Dominio: ERP Sistémico (Contable)
GovernanceKernel.register_intention(GovernanceIntention(
    name="ERP_GENERATE_BALANCE",
    domain="contable",
    required_role=CustomUser.Role.ADMIN
))
