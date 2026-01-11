"""
Módulo de Enrutamiento a Capitanes para Gobernanza Municipal.

Asigna tareas tácticas (ej. validación de documentos, inspecciones)
a los Capitanes especializados del dominio municipal.
"""

from typing import Dict, Any

class GubernamentalMunicipalCaptainRouter:
    """
    Asigna tareas tácticas a los Capitanes del municipio.
    """

    def __init__(self):
        """
        Inicializa el router con el registro de capitanes municipales.
        """
        self._captain_registry = {
            "validacion_documental": "CapitanAgente_ArchivisticaMunicipal_ID_M01",
            "consulta_externa": "CapitanAgente_IntegracionNacional_ID_M02",
            "consulta_financiera_interna": "CapitanAgente_HaciendaMunicipal_ID_M03",
            "logistica": "CapitanAgente_Planeacion_ID_M04",
            "inspeccion_campo": "CapitanAgente_ObrasPublicas_ID_M05",
            "default": "CapitanAgente_VentanillaUnica_ID_M99"
        }
        print("CAPTAIN ROUTER: Router de Capitanes Gubernamental Municipal inicializado.")
        print(f"CAPTAIN ROUTER: {len(self._captain_registry)} capitanes municipales registrados.")

    def route_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Determina el capitán correcto y prepara la asignación de la tarea.
        """
        required_capability = task.get("capitan_requerido", "default")

        print(f"CAPTAIN ROUTER: Enrutando tarea tipo '{task.get('type')}' que requiere '{required_capability}'.")

        target_captain_id = self._captain_registry.get(required_capability)

        if not target_captain_id:
            print(f"CAPTAIN ROUTER: ¡Alerta! Capacidad '{required_capability}' no encontrada. Usando capitán por defecto.")
            target_captain_id = self._captain_registry["default"]

        assignment = {
            "target_captain_id": target_captain_id,
            "task_payload": task,
            "status": "READY_TO_DISPATCH"
        }

        print(f"CAPTAIN ROUTER: Tarea asignada al Capitán ID '{target_captain_id}'.")
        return assignment

# Ejemplo de uso
if __name__ == '__main__':
    router = GubernamentalMunicipalCaptainRouter()

    tareas = [
        {"type": "verificar_documento_adjunto", "documento": "uso_de_suelo", "capitan_requerido": "validacion_documental"},
        {"type": "ejecutar_checklist_inspeccion", "tipo_checklist": "sanitario", "capitan_requerido": "inspeccion_campo"},
        {"type": "enviar_notificacion_email", "destinatario": "test@test.com", "capitan_requerido": "comunicaciones"} # Capacidad no existente
    ]

    print("\n--- Proceso de Enrutamiento de Tareas Municipales ---")
    for tarea in tareas:
        router.route_task(tarea)
        print("-" * 10)
