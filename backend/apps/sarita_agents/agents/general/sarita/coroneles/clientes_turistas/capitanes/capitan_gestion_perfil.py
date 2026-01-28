from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanGestionPerfil(CapitanTemplate):
    """
    Misión: Administrar el perfil del turista, incluyendo sus datos personales,
    preferencias de viaje, historial de reservas y configuración de
    notificaciones, garantizando la privacidad y personalización.
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
            nombre=f"Plan de Gestión de Perfil",
            descripcion=f"Gestionar perfil para el objetivo: {self.objective}"
        )

        self.delegar_tarea(
            plan_tactico=plan_tactico,
            nombre_teniente="gestion_perfil",
            descripcion="Realizar operaciones sobre el perfil del turista.",
            parametros_especificos=self.parametros
        )

        self.lanzar_ejecucion_plan()
        self.logger.info(f"CAPITÁN {self.__class__.__name__}: Planificación completada y tarea delegada a 'gestion_perfil'.")
