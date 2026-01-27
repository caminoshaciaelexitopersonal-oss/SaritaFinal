# backend/apps/sarita_agents/agents/capitan_template.py
 
import logging
from celery import group, chord
from backend.apps.sarita_agents.models import Mision, PlanTáctico, TareaDelegada
from backend.tasks import ejecutar_tarea_teniente, consolidar_plan_tactico

logger = logging.getLogger(__name__)
 

class CapitanTemplate:
    """
    Plantilla base para todos los Capitanes.
    Define el ciclo de vida de planificación, delegación y reporte.
    """
    def __init__(self, coronel):
        self.coronel = coronel
        self.tenientes = self._get_tenientes()
 
        logger.info(f"CAPITÁN ({self.__class__.__name__}): Inicializado. Tenientes listos.")
 

    def handle_order(self, mision: Mision):
        """
        Recibe una orden (misión) del Coronel, la procesa y gestiona su ejecución.
        """
 
        logger.info(f"CAPITÁN ({self.__class__.__name__}): Orden recibida para misión {mision.id}")

        plan = self.plan(mision)
        # El método delegate ahora es asíncrono y no devuelve resultados directamente.
        self.delegate(plan)

        # El reporte se genera y envía de forma asíncrona por la tarea de consolidación.
        # Devolvemos un reporte intermedio.
        return {
            "status": "PROCESSING",
            "message": f"El plan {plan.id} ha sido encolado para ejecución asíncrona."
        }
 

    def plan(self, mision: Mision) -> PlanTáctico:
        """
        Crea un plan táctico para cumplir la misión y lo persiste en la BD.
        Este método debe ser implementado por cada Capitán concreto.
        """
        raise NotImplementedError("El método plan() debe ser implementado por cada Capitán.")

 
    def delegate(self, plan: PlanTáctico):
        """
        Crea un grupo de tareas de tenientes y las ejecuta en un chord.
        El callback del chord se encargará de la consolidación.
        """
        logger.info(f"CAPITÁN ({self.__class__.__name__}): Construyendo chord para el plan {plan.id}...")
        plan.estado = 'EN_EJECUCION'
        plan.save()

        header = []
        for _, tarea_info in plan.pasos_del_plan.items():
 
            tarea = TareaDelegada.objects.create(
                plan_tactico=plan,
                teniente_asignado=tarea_info.get("teniente", "default"),
                descripcion_tarea=tarea_info.get("descripcion", "N/A"),
 
                parametros=tarea_info.get("parametros", {}),
                estado='EN_COLA'
            )
            header.append(ejecutar_tarea_teniente.s(tarea_id=str(tarea.id)))

        callback = consolidar_plan_tactico.s(plan_id=str(plan.id))

        # Crear y ejecutar el chord
        chord(group(header))(callback)

        logger.info(f"Chord para el plan {plan.id} ha sido encolado.")
 

    def _get_tenientes(self) -> dict:
        """
        Carga el roster de Tenientes bajo el mando de este Capitán.
        Este método debe ser implementado por cada Capitán concreto.
        """
        raise NotImplementedError("El método _get_tenientes() debe ser implementado por cada Capitán.")
