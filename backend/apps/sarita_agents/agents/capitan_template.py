# backend/apps/sarita_agents/agents/capitan_template.py

from apps.sarita_agents.models import Mision, PlanTáctico, TareaDelegada

class CapitanTemplate:
    """
    Plantilla base para todos los Capitanes.
    Define el ciclo de vida de planificación, delegación y reporte.
    """
    def __init__(self, coronel):
        self.coronel = coronel
        self.tenientes = self._get_tenientes()
        print(f"CAPITÁN ({self.__class__.__name__}): Inicializado. Tenientes listos.")

    def handle_order(self, mision: Mision):
        """
        Recibe una orden (misión) del Coronel, la procesa y gestiona su ejecución.
        """
        print(f"CAPITÁN ({self.__class__.__name__}): Orden recibida para misión {mision.id}")

        plan = self.plan(mision)
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self, mision: Mision) -> PlanTáctico:
        """
        Crea un plan táctico para cumplir la misión y lo persiste en la BD.
        Este método debe ser implementado por cada Capitán concreto.
        """
        raise NotImplementedError("El método plan() debe ser implementado por cada Capitán.")

    def delegate(self, plan: PlanTáctico) -> dict:
        """
        Delega la ejecución de los pasos del plan a los Tenientes.
        """
        print(f"CAPITÁN ({self.__class__.__name__}): Delegando tareas del plan {plan.id}...")
        results = {}
        for paso, tarea_info in plan.pasos_del_plan.items():

            # 1. Crear la TareaDelegada en la BD
            tarea = TareaDelegada.objects.create(
                plan_tactico=plan,
                teniente_asignado=tarea_info.get("teniente", "default"),
                descripcion_tarea=tarea_info.get("descripcion", "N/A"),
                parametros=tarea_info.get("parametros", {})
            )

            # 2. Asignar y ejecutar
            teniente = self.tenientes.get(tarea.teniente_asignado)
            if teniente:
                print(f"  - Delegando tarea {tarea.id} a Teniente '{tarea.teniente_asignado}'")
                resultado = teniente.execute_task(tarea)
                results[paso] = resultado
            else:
                results[paso] = {"error": f"Teniente '{tarea.teniente_asignado}' no encontrado."}

        return results

    def report(self, delegation_results: dict) -> dict:
        """
        Prepara el informe final para el Coronel.
        """
        print(f"CAPITÁN ({self.__class__.__name__}): Preparando informe final.")
        return {
            "captain": self.__class__.__name__,
            "status": "COMPLETED",
            "details": delegation_results
        }

    def _get_tenientes(self) -> dict:
        """
        Carga el roster de Tenientes bajo el mando de este Capitán.
        Este método debe ser implementado por cada Capitán concreto.
        """
        raise NotImplementedError("El método _get_tenientes() debe ser implementado por cada Capitán.")
