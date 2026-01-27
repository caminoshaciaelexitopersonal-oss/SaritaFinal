from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanSeguridadAccesos(CapitanTemplate):
    """
    Misión: Controlar y gestionar la seguridad de la plataforma, incluyendo
    la autenticación de usuarios, la gestión de roles y permisos (RBAC),
    y la detección de actividades sospechosas o no autorizadas.
    """

    def __init__(self, mision_id: str, objective: str, parametros: Dict[str, Any]):
        super().__init__(mision_id=mision_id, objective=objective, parametros=parametros)
        self.logger.info(f"CAPITÁN {self.__class__.__name__}: Inicializado para Misión ID {self.mision_id}.")

    def plan(self):
        """
        El corazón del Capitán. Aquí es donde defines el plan táctico.
        """
        self.logger.info(f"CAPITÁN {self.__class__.__name__}: Planificando la misión.")

        plan_tactico = self.get_or_create_plan_tactico(
            nombre=f"Plan de Seguridad y Accesos",
            descripcion=f"Aplicar políticas de seguridad para el objetivo: {self.objective}"
        )

        self.delegar_tarea(
            plan_tactico=plan_tactico,
            nombre_teniente="seguridad_accesos",
            descripcion="Ejecutar las políticas de seguridad y control de acceso.",
            parametros_especificos=self.parametros
        )

        self.lanzar_ejecucion_plan()
        self.logger.info(f"CAPITÁN {self.__class__.__name__}: Planificación completada y tarea delegada a 'seguridad_accesos'.")
