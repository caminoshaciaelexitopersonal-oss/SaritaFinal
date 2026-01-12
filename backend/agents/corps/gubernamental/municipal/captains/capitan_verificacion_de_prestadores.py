from typing import Dict, Any, List

# Base de datos simulada para el estado de verificación de prestadores
PRESTADORES_REGISTRO: Dict[str, Dict[str, Any]] = {
    "prestador_01": {"nombre": "Hotel El Mirador del Llano", "estado": "PENDIENTE_DOCUMENTOS"},
    "prestador_02": {"nombre": "Safari por los Llanos", "estado": "VERIFICADO"},
    "prestador_03": {"nombre": "La Mamona del Abuelo", "estado": "RECHAZADO"},
}


class CapitanVerificacionDePrestadores:
    """
    Capitán encargado de verificar los documentos y el cumplimiento
    de los prestadores de servicios turísticos a nivel municipal.
    """

    def __init__(self):
        print("CAPITÁN VERIFICACIÓN DE PRESTADORES (MUNICIPAL): Inicializado.")
        self.registro = PRESTADORES_REGISTRO

    def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task.get("type")
        params = task.get("params", {})
        print(f"CAPITÁN VERIFICACIÓN: Ejecutando tarea '{task_type}' con params: {params}")

        if task_type == "consultar_estado":
            return self._handle_consultar_estado(params)
        elif task_type == "actualizar_estado":
            return self._handle_actualizar_estado(params)
        else:
            return {"status": "ERROR", "result": f"Tipo de tarea '{task_type}' no reconocida."}

    def _handle_consultar_estado(self, params: Dict[str, Any]) -> Dict[str, Any]:
        prestador_id = params.get("prestador_id")
        if not prestador_id:
            return {"status": "ERROR", "result": "El parámetro 'prestador_id' es requerido."}

        prestador = self.registro.get(prestador_id)
        if prestador:
            return {"status": "SUCCESS", "result": prestador}
        else:
            return {"status": "NOT_FOUND", "result": f"Prestador con id '{prestador_id}' no encontrado."}

    def _handle_actualizar_estado(self, params: Dict[str, Any]) -> Dict[str, Any]:
        prestador_id = params.get("prestador_id")
        nuevo_estado = params.get("nuevo_estado")

        if not all([prestador_id, nuevo_estado]):
            return {"status": "ERROR", "result": "Los parámetros 'prestador_id' y 'nuevo_estado' son requeridos."}

        if prestador_id not in self.registro:
            return {"status": "NOT_FOUND", "result": f"Prestador con id '{prestador_id}' no encontrado."}

        self.registro[prestador_id]["estado"] = nuevo_estado
        print(f"CAPITÁN VERIFICACIÓN: Estado del prestador '{prestador_id}' actualizado a '{nuevo_estado}'.")
        return {"status": "SUCCESS", "result": self.registro[prestador_id]}
