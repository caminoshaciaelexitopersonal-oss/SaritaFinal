"""
Módulo de Enrutamiento a Capitanes para el Coronel SG-SST.

Este componente es el responsable de la logística táctica. Recibe una tarea
atómica del Decomposer y, basándose en las capacidades requeridas, la asigna
al Capitán más idóneo para su ejecución.
"""

from typing import Dict, Any

class SSTCaptainRouter:
    """
    Asigna tareas tácticas a los Capitanes especializados.
    """

    def __init__(self):
        """
        Inicializa el router y el registro de capitanes.

        En un sistema real, este registro podría cargarse dinámicamente o
        ser parte de una arquitectura de descubrimiento de servicios.
        """
        # Simulación de un registro de capitanes disponibles.
        # Las "instancias" serían objetos reales de las clases Capitán.
        self._captain_registry = {
            "documentacion": "CapitanAgente_GestorDocumental_ID_A45",
            "verificacion": "CapitanAgente_VerificadorNormativo_ID_B72",
            "inspeccion_campo": "CapitanAgente_InspectorDeCampo_ID_C91",
            "inspeccion_equipos": "CapitanAgente_EspecialistaEquipos_ID_D13",
            "default": "CapitanAgente_OperacionesGenerales_ID_Z01"
        }
        print("CAPTAIN ROUTER: Router de Capitanes SG-SST inicializado.")
        print(f"CAPTAIN ROUTER: {len(self._captain_registry)} capitanes registrados y listos.")

    def route_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Determina el capitán correcto y prepara la asignación de la tarea.

        Args:
            task (Dict[str, Any]): La tarea táctica con sus detalles, incluyendo
                                   la clave 'capitan_requerido'.

        Returns:
            Dict[str, Any]: Un diccionario de asignación con el ID del capitán
                            y la tarea a ejecutar, o un error si no se encuentra
                            un capitán adecuado.
        """
        required_capability = task.get("capitan_requerido", "default")

        print(f"CAPTAIN ROUTER: Enrutando tarea tipo '{task.get('type')}' que requiere capacidad '{required_capability}'.")

        target_captain_id = self._captain_registry.get(required_capability)

        if not target_captain_id:
            print(f"CAPTAIN ROUTER: ¡Alerta! No se encontró un capitán con la capacidad '{required_capability}'. Usando capitán por defecto.")
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
    # 1. Instanciar el router
    router = SSTCaptainRouter()

    # 2. Definir un conjunto de tareas (simulando la salida del Decomposer)
    tareas_para_enrutar = [
        {"type": "solicitar_documento", "documento": "matriz_riesgos_actualizada", "capitan_requerido": "documentacion"},
        {"type": "inspeccionar_area", "area": "cocina", "checklist": "general_seguridad", "capitan_requerido": "inspeccion_campo"},
        {"type": "tarea_desconocida", "details": "...", "capitan_requerido": "robotica_avanzada"} # Simula una capacidad no existente
    ]

    print("\n--- Proceso de Enrutamiento de Tareas ---")
    for i, tarea in enumerate(tareas_para_enrutar, 1):
        print(f"\n{i}. Procesando tarea:")
        asignacion = router.route_task(tarea)
        print(f"   -> Resultado de Asignación: {asignacion}")
    print("\n-----------------------------------------")
