# backend/apps/sarita_agents/agents/archivistica/coronel_archivistico_general.py
# CORONEL ARCHIVÍSTICO GENERAL (1)
# FASE 2.1 — VALIDACIÓN ESTRUCTURAL TOTAL

import logging
from apps.sarita_agents.agents.archivistica_base_templates import AgenteArchivisticoBase

logger = logging.getLogger(__name__)

class CoronelArchivisticoGeneral(AgenteArchivisticoBase):
    """
    CORONEL ARCHIVÍSTICO GENERAL
    Rol: Autoridad Máxima Archivística
    Dominio: GESTION_ARCHIVISTICA
    Superior: GeneralSarita
    Responsabilidad: Gobernar toda la política documental de SARITA.
    """
    nivel = "CORONEL_GENERAL"
    dominio = "GESTION_ARCHIVISTICA"
    superior = "GeneralSarita"
    responsabilidad_unica = "Gobernar toda la política documental y garantizar la inmutabilidad de la memoria institucional."

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.capitanes = self._get_capitanes()
        self.politicas_globales = self._load_politicas()
        logger.info("CORONEL ARCHIVÍSTICO GENERAL: Estructura de mando inicializada.")

    def _get_capitanes(self) -> dict:
        """Registro explícito de Capitanes bajo su mando."""
        return {
            "captura": "CapitanCapturaDocumental",
            "clasificacion": "CapitanClasificacionMetadatos",
            "custodia": "CapitanCustodiaAlmacenamiento",
            "acceso": "CapitanAccesoConsulta",
            "versionado": "CapitanVersionadoTrazabilidad",
            "conservacion": "CapitanConservacionRetencion",
            "eliminacion": "CapitanEliminacionGobernada",
            "auditoria": "CapitanAuditoriaArchivistica"
        }

    def _load_politicas(self) -> List[str]:
        """Carga de políticas archivísticas globales."""
        return [
            "POLITICA_CERO_BORRADO_NO_AUDITADO",
            "POLITICA_HASH_OBLIGATORIO",
            "POLITICA_TRAZABILIDAD_TOTAL"
        ]

    def bitacora_activa(self):
        """Estado de la bitácora de gobernanza."""
        return True
