"""
Agente Capitán Táctico: CapitanGestionClientes

Responsable de ejecutar tareas atómicas relacionadas con la gestión de clientes (CRM).
"""

from typing import Dict, Any
import uuid

# Simulación de una base de datos de clientes en memoria.
# En un sistema real, esto sería reemplazado por llamadas a un servicio o a la base de datos de Django.
CLIENTES_DB = {}

class CapitanGestionClientes:
    """
    Ejecuta tareas tácticas de gestión de clientes asignadas por un Coronel.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Punto de entrada principal que enruta la tarea al método correcto.
        """
        task_type = task_payload.get("type")
        print(f"CAPITAN GESTION CLIENTES: Recibida tarea táctica '{task_type}'.")

        handler_method = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler_method(task_payload)

    def _handle_crear_cliente(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Lógica para crear un nuevo cliente en el sistema.
        """
        datos_cliente = task_data.get("datos_cliente", {})
        nombre = datos_cliente.get("nombre")
        email = datos_cliente.get("email")

        if not nombre or not email:
            return {"status": "FAILED", "error": "Datos incompletos. Se requiere nombre y email."}

        print(f"CAPITAN GESTION CLIENTES: Creando cliente '{nombre}' con email '{email}'.")

        cliente_id = f"CLI-{uuid.uuid4().hex[:6].upper()}"
        CLIENTES_DB[cliente_id] = {
            "id": cliente_id,
            "nombre": nombre,
            "email": email,
            "telefono": datos_cliente.get("telefono"),
            "fecha_registro": "2024-01-01T12:00:00Z" # Simulado
        }

        print(f"CAPITAN GESTION CLIENTES: Cliente '{cliente_id}' creado exitosamente.")
        return {
            "status": "COMPLETED",
            "result": {"cliente_id": cliente_id, "mensaje": "Cliente creado exitosamente."}
        }

    def _handle_actualizar_datos_cliente(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Lógica para actualizar los datos de un cliente existente.
        """
        cliente_id = task_data.get("cliente_id")
        nuevos_datos = task_data.get("nuevos_datos", {})

        if not cliente_id or cliente_id not in CLIENTES_DB:
            return {"status": "FAILED", "error": f"Cliente con ID '{cliente_id}' no encontrado."}

        print(f"CAPITAN GESTION CLIENTES: Actualizando datos para el cliente '{cliente_id}'.")
        CLIENTES_DB[cliente_id].update(nuevos_datos)

        return {
            "status": "COMPLETED",
            "result": {"cliente_id": cliente_id, "mensaje": "Datos del cliente actualizados."}
        }

    def _handle_consultar_cliente_por_id(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Lógica para consultar la información de un cliente por su ID.
        """
        cliente_id = task_data.get("cliente_id")

        if not cliente_id or cliente_id not in CLIENTES_DB:
            return {"status": "FAILED", "error": f"Cliente con ID '{cliente_id}' no encontrado."}

        print(f"CAPITAN GESTION CLIENTES: Consultando datos del cliente '{cliente_id}'.")
        return {
            "status": "COMPLETED",
            "result": {"cliente_data": CLIENTES_DB[cliente_id]}
        }

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Maneja tareas desconocidas para este capitán."""
        task_type = task_data.get("type")
        return {
            "status": "FAILED",
            "error": f"El CapitanGestionClientes no puede manejar la tarea de tipo '{task_type}'."
        }

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanGestionClientes()

    # 1. Crear un cliente
    tarea_crear = {
        "type": "crear_cliente",
        "datos_cliente": {"nombre": "Juan Pérez", "email": "juan.perez@example.com", "telefono": "555-1234"}
    }
    resultado_crear = capitan.execute_task(tarea_crear)
    print("Resultado Crear:", resultado_crear)

    print("\nBD de Clientes:", CLIENTES_DB)
    print("-" * 20)

    # 2. Actualizar el cliente
    cliente_id = resultado_crear.get("result", {}).get("cliente_id")
    tarea_actualizar = {
        "type": "actualizar_datos_cliente",
        "cliente_id": cliente_id,
        "nuevos_datos": {"telefono": "555-5678", "ciudad": "Bogotá"}
    }
    resultado_actualizar = capitan.execute_task(tarea_actualizar)
    print("Resultado Actualizar:", resultado_actualizar)

    print("\nBD de Clientes:", CLIENTES_DB)
    print("-" * 20)

    # 3. Consultar el cliente
    tarea_consultar = {"type": "consultar_cliente_por_id", "cliente_id": cliente_id}
    resultado_consultar = capitan.execute_task(tarea_consultar)
    print("Resultado Consultar:", resultado_consultar)
