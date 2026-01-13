from typing import Dict, Any

class TenienteRegistroClientes:
    """
    Rol: Realizar el alta inicial de un cliente en el sistema (CRM).
    Capitán Superior: capitan_gestion_clientes
    Tipo de Tareas:
      - recibir_datos_cliente
      - validar_formato_datos
      - crear_nuevo_id_cliente
      - guardar_registro_inicial
    """
    def __init__(self, capitan):
        self.capitan = capitan

    def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        print(f"TENIENTE REGISTRO CLIENTES: Ejecutando tarea {task['type']}")
        return {"status": "SUCCESS", "result": "Tarea de registro de cliente completada."}
