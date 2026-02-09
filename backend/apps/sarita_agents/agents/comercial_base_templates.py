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

    def validar_jerarquia(self, nivel_requerido=None):
        """Validación obligatoria antes de cualquier acción."""
        from apps.admin_plataforma.services.governance_kernel import GovernanceKernel

        # 0. Verificar si el nivel es el correcto para la acción
        if nivel_requerido and self.nivel != nivel_requerido:
            self.penalizar_confianza("ABUSO_DE_PODER", f"Agente de nivel {self.nivel} intentó ejecutar acción de nivel {nivel_requerido}")
            raise PermissionError(f"SABOTAJE DETECTADO: El agente {self.__class__.__name__} ({self.nivel}) intentó ejecutar una acción de nivel {nivel_requerido}.")

        # 1. Verificar estado activo
        if not self.is_active():
            raise PermissionError(f"ERROR JERÁRQUICO: El agente {self.__class__.__name__} está DESHABILITADO.")

        # 2. Verificar integridad de superior
        if not self.verificar_superior():
            raise PermissionError(f"ERROR JERÁRQUICO: Superior {self.superior} inactivo. Cadena de mando rota.")

        # 3. Verificar score de confianza
        agent_data = GovernanceKernel._agent_registry.get(self.__class__.__name__, {})
        if agent_data.get("trust_score", 100) < 20:
             logger.critical(f"NODO CORRUPTO AISLADO: {self.__class__.__name__} tiene score crítico y ha sido bloqueado.")
             GovernanceKernel.alternar_estado_agente(self.__class__.__name__, "AISLADO")
             raise PermissionError(f"RESILIENCIA: Agente {self.__class__.__name__} aislado por baja confiabilidad.")

    def penalizar_confianza(self, tipo, motivo):
        """Disminuye el score de confianza y registra la violación."""
        from apps.admin_plataforma.services.governance_kernel import GovernanceKernel
        GovernanceKernel.penalizar_agente(self.__class__.__name__, tipo, motivo)

class CapitanComercialBase(AgenteComercialBase):
    nivel = "CAPITAN"

    def plan(self, mision_obj):
        self.validar_jerarquia(nivel_requerido="CAPITAN")
        if not mision_obj:
            self.penalizar_confianza("OMISION", "Capitán recibió misión nula o se negó a autorizar")
            return {"status": "BLOCKED", "reason": "No authorization"}

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
        self.validar_jerarquia(nivel_requerido="TENIENTE")
        logger.info(f"TENIENTE {self.__class__.__name__}: Coordinando táctica y Sargentos.")
        return {"status": "COORDINATED", "agent": self.__class__.__name__}

    def verificar_resultado_sargento(self, sargento_id, resultado):
        """FASE 1.3: Verificación cruzada del Teniente sobre el Sargento."""
        if not resultado or resultado.get("status") != "SUCCESS":
            self.penalizar_confianza("SARGENTO_FALLIDO", f"El sargento {sargento_id} reportó fallo o inconsistencia")
            return False
        return True

class SargentoComercialBase(AgenteComercialBase):
    nivel = "SARGENTO"

    def ejecutar(self, action_data):
        self.validar_jerarquia(nivel_requerido="SARGENTO")
        # Simular detección de manipulación
        if action_data.get("manipulado") is True:
             self.penalizar_confianza("MANIPULACION", "Intento de alteración de resultados atómicos")
             return {"status": "ERROR", "message": "Integrity violation"}

        logger.info(f"SARGENTO {self.__class__.__name__}: Ejecutando acción atómica y orquestando Soldados.")
        return {"status": "EXECUTED", "agent": self.__class__.__name__, "data": action_data}

class SoldadoComercialBase(AgenteComercialBase):
    nivel = "SOLDADO"

    def realizar_tarea_manual(self, orden_data):
        self.validar_jerarquia(nivel_requerido="SOLDADO")
        # Si el soldado intenta reportar éxito sin datos
        if not orden_data:
             self.penalizar_confianza("FALSIFICACION", "Soldado reportó éxito sin evidencia")
             return {"status": "ERROR", "message": "No evidence provided"}

        logger.info(f"SOLDADO {self.__class__.__name__}: Ejecutando orden manual única.")
        return {"status": "MANUAL_DONE", "agent": self.__class__.__name__}
