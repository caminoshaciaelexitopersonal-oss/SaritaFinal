from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanSeguridadAccesos(CapitanTemplate):
    """
    Misión: Controlar y gestionar la seguridad de la plataforma, incluyendo
    la autenticación de usuarios, la gestión de roles y permisos (RBAC),
    y la detección de actividades sospechosas o no autorizadas.
    """

    def __init__(self, coronel):
        super().__init__(coronel=coronel)
        logger.info(f"CAPITÁN {self.__class__.__name__}: Inicializado para Misión ID {mision.id}.")

    def plan(self, mision):
        """
        El corazón del Capitán. Aquí es donde defines el plan táctico.
        """
        logger.info(f"CAPITÁN {self.__class__.__name__}: Planificando la misión.")

        plan_tactico = self.coronel.get_or_create_plan_tactico(
            nombre=f"Plan de Seguridad y Accesos",
            descripcion=f"Aplicar políticas de seguridad para el objetivo: {mision.directiva_original.get('objective', 'N/A')}"
        )

        self.delegar_tarea(
            plan_tactico=plan_tactico,
            nombre_teniente="seguridad_accesos",
            descripcion="Ejecutar las políticas de seguridad y control de acceso.",
            parametros_especificos=self.parametros
        )

        # self.lanzar_ejecucion_plan() handled by template
        logger.info(f"CAPITÁN {self.__class__.__name__}: Planificación completada y tarea delegada a 'seguridad_accesos'.")
