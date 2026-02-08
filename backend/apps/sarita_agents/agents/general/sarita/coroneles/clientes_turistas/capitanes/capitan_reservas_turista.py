from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanReservasTurista(CapitanTemplate):
    """
    Misión: Gestionar el ciclo de vida de las reservas de un turista,
    desde la creación y confirmación hasta la modificación o cancelación,
    asegurando la comunicación con los prestadores de servicios.
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
            nombre=f"Plan de Gestión de Reservas",
            descripcion=f"Gestionar reserva para el objetivo: {mision.directiva_original.get('objective', 'N/A')}"
        )

        self.delegar_tarea(
            plan_tactico=plan_tactico,
            nombre_teniente="reservas_turista",
            descripcion="Realizar operaciones sobre la reserva de un turista.",
            parametros_especificos=self.parametros
        )

        # self.lanzar_ejecucion_plan() handled by template
        logger.info(f"CAPITÁN {self.__class__.__name__}: Planificación completada y tarea delegada a 'reservas_turista'.")
