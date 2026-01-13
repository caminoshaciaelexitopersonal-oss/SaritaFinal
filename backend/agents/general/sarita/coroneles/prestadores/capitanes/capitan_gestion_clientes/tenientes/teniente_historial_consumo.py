from typing import Dict, Any

class TenienteHistorialConsumo:
    """
    Rol: Registrar los servicios y productos consumidos por un cliente.
    Capitán Superior: capitan_gestion_clientes
    Tipo de Tareas:
      - recibir_notificacion_consumo
      - asociar_consumo_a_cliente
      - actualizar_perfil_de_gasto
      - registrar_fecha_ultimo_consumo
    """
    def __init__(self, capitan):
        self.capitan = capitan

    def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        print(f"TENIENTE HISTORIAL CONSUMO: Ejecutando tarea {task['type']}")
        return {"status": "SUCCESS", "result": "Tarea de historial de consumo completada."}
