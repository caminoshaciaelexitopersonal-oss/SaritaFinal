# backend/apps/sarita_agents/agents/archivistica_base_templates.py
# Plantilla Maestra para la FASE 2.1 — Gestión Archivística

import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)

class AgenteArchivisticoBase:
    """
    Base para todos los agentes del dominio de Gestión Archivística.
    Garantiza la jerarquía, el registro en el Kernel y la inmutabilidad documental.
    """
    nivel = None
    dominio = "GESTION_ARCHIVISTICA"
    superior = None
    mision = None
    eventos = []
    responsabilidad_unica = ""

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
        """Verifica la cadena de mando."""
        if not self.superior or self.superior == "CoronelArchivisticoGeneral" or self.superior == "GeneralSarita":
            return True

        from apps.admin_plataforma.services.governance_kernel import GovernanceKernel
        superior_data = GovernanceKernel._agent_registry.get(self.superior, {})
        return superior_data.get("estado") == "ACTIVO"

    def validar_estructura(self):
        """Validación de existencia y herencia para la FASE 2.1."""
        if not self.nivel:
            raise ValueError(f"FALLA ESTRUCTURAL: {self.__class__.__name__} no tiene nivel definido.")
        if not self.superior:
            raise ValueError(f"FALLA ESTRUCTURAL: {self.__class__.__name__} no tiene superior definido.")
        if not self.responsabilidad_unica:
            raise ValueError(f"FALLA ESTRUCTURAL: {self.__class__.__name__} no tiene responsabilidad única definida.")

class CapitanArchivisticoBase(AgenteArchivisticoBase):
    nivel = "CAPITAN"

    def _get_tenientes(self) -> dict:
        raise NotImplementedError("Cada Capitán debe declarar sus Tenientes explícitamente.")

class TenienteArchivisticoBase(AgenteArchivisticoBase):
    nivel = "TENIENTE"

    def _get_sargentos(self) -> dict:
        raise NotImplementedError("Cada Teniente debe declarar sus Sargentos explícitamente.")

class SargentoArchivisticoBase(AgenteArchivisticoBase):
    nivel = "SARGENTO"

    def _get_soldados(self) -> List[str]:
        raise NotImplementedError("Cada Sargento debe tener exactamente 5 Soldados.")

class SoldadoArchivisticoBase(AgenteArchivisticoBase):
    nivel = "SOLDADO"
    tarea_manual = ""

    def validar_tarea(self):
        if not self.tarea_manual:
            raise ValueError(f"FALLA ESTRUCTURAL: Soldado {self.__class__.__name__} no tiene tarea manual definida.")
