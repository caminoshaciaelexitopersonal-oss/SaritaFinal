# backend/apps/sarita_agents/agents/comercial_base_templates.py

import logging

logger = logging.getLogger(__name__)

class AgenteComercialBase:
    nivel = None
    dominio = "GESTION_COMERCIAL"
    superior = None
    mision = None
    eventos = []
    dependencias = []

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        logger.info(f"AGENTE {self.nivel} ({self.__class__.__name__}): Inicializado.")

    def is_active(self) -> bool:
        """Verifica si el agente está habilitado en el Kernel."""
        from apps.admin_plataforma.services.governance_kernel import GovernanceKernel
        agent_data = GovernanceKernel._agent_registry.get(self.__class__.__name__, {})
        return agent_data.get("estado") == "ACTIVO"

    def verificar_superior(self) -> bool:
        """Verifica si el superior inmediato está activo."""
        if not self.superior or self.superior == "CoronelComercialGeneral":
            return True # El Coronel General se asume activo o se valida por estado sistémico

        from apps.admin_plataforma.services.governance_kernel import GovernanceKernel
        superior_data = GovernanceKernel._agent_registry.get(self.superior, {})
        is_sup_active = superior_data.get("estado") == "ACTIVO"

        if not is_sup_active:
            logger.error(f"BLOQUEO JERÁRQUICO: {self.__class__.__name__} no puede actuar porque su superior {self.superior} está INACTIVO.")
        return is_sup_active

    def validar_jerarquia(self):
        """Validación obligatoria antes de cualquier acción."""
        if not self.is_active():
            raise PermissionError(f"ERROR JERÁRQUICO: El agente {self.__class__.__name__} está DESHABILITADO.")
        if not self.verificar_superior():
            raise PermissionError(f"ERROR JERÁRQUICO: Superior {self.superior} inactivo. Cadena de mando rota.")

class CapitanComercialBase(AgenteComercialBase):
    nivel = "CAPITAN"

    def plan(self, mision_obj):
        self.validar_jerarquia()
        logger.info(f"CAPITAN {self.__class__.__name__}: Planificando misión estratégica.")
        return {"status": "PLANIFIED", "agent": self.__class__.__name__}

    def supervisar_cadena(self):
        """Listar subordinados y su estado."""
        from apps.admin_plataforma.services.governance_kernel import GovernanceKernel
        subordinados = [
            data for name, data in GovernanceKernel._agent_registry.items()
            if data.get("superior") == self.__class__.__name__
        ]
        return subordinados

    def alternar_subordinado(self, subordinado_id: str, habilitar: bool):
        """Habilitar o deshabilitar un subordinado directo."""
        from apps.admin_plataforma.services.governance_kernel import GovernanceKernel
        nuevo_estado = "ACTIVO" if habilitar else "DESHABILITADO"
        GovernanceKernel.alternar_estado_agente(
            agent_id=subordinado_id,
            nuevo_estado=nuevo_estado,
            caller_agent_id=self.__class__.__name__
        )

    def auditar_subordinados(self):
        """Auditar acciones de todos los subordinados."""
        from apps.sarita_agents.models import RegistroDeEjecucion
        # Simplificado: obtener los últimos logs de tareas delegadas a sus tenientes
        tenientes = [s["id"] for s in self.supervisar_cadena()]
        logs = RegistroDeEjecucion.objects.filter(
            tarea_delegada__teniente_asignado__in=tenientes
        ).order_by('-timestamp')[:50]

        return logs

class TenienteComercialBase(AgenteComercialBase):
    nivel = "TENIENTE"

    def coordinar(self, parametros):
        self.validar_jerarquia()
        logger.info(f"TENIENTE {self.__class__.__name__}: Coordinando táctica y Sargentos.")
        return {"status": "COORDINATED", "agent": self.__class__.__name__}

class SargentoComercialBase(AgenteComercialBase):
    nivel = "SARGENTO"

    def ejecutar(self, action_data):
        self.validar_jerarquia()
        logger.info(f"SARGENTO {self.__class__.__name__}: Ejecutando acción atómica y orquestando Soldados.")
        return {"status": "EXECUTED", "agent": self.__class__.__name__}

class SoldadoComercialBase(AgenteComercialBase):
    nivel = "SOLDADO"

    def realizar_tarea_manual(self, orden_data):
        self.validar_jerarquia()
        logger.info(f"SOLDADO {self.__class__.__name__}: Ejecutando orden manual única.")
        return {"status": "MANUAL_DONE", "agent": self.__class__.__name__}
