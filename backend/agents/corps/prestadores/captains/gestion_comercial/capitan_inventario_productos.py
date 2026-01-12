"""
Agente Capitán Táctico: CapitanInventarioProductos

Responsable de ejecutar tareas atómicas relacionadas con la gestión de
productos, servicios y su disponibilidad (inventario).
"""

from typing import Dict, Any
import uuid

# Simulación de una base de datos de productos/inventario en memoria.
PRODUCTOS_DB = {}

class CapitanInventarioProductos:
    """
    Ejecuta tareas tácticas de gestión de inventario asignadas por un Coronel.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Punto de entrada principal que enruta la tarea al método correcto.
        """
        task_type = task_payload.get("type")
        print(f"CAPITAN INVENTARIO: Recibida tarea táctica '{task_type}'.")

        handler_method = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler_method(task_payload)

    def _handle_crear_producto(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Lógica para crear un nuevo producto o servicio en el inventario.
        """
        datos_producto = task_data.get("datos_producto", {})
        nombre = datos_producto.get("nombre")
        precio = datos_producto.get("precio")
        stock_inicial = datos_producto.get("stock_disponible", 0)

        if not nombre or precio is None:
            return {"status": "FAILED", "error": "Datos incompletos. Se requiere nombre y precio."}

        print(f"CAPITAN INVENTARIO: Creando producto '{nombre}' con precio '{precio}' y stock '{stock_inicial}'.")

        producto_id = f"PROD-{uuid.uuid4().hex[:6].upper()}"
        PRODUCTOS_DB[producto_id] = {
            "id": producto_id,
            "nombre": nombre,
            "descripcion": datos_producto.get("descripcion", ""),
            "precio": float(precio),
            "stock_disponible": int(stock_inicial)
        }

        print(f"CAPITAN INVENTARIO: Producto '{producto_id}' creado exitosamente.")
        return {
            "status": "COMPLETED",
            "result": {"producto_id": producto_id, "mensaje": "Producto creado exitosamente."}
        }

    def _handle_actualizar_stock(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Lógica para actualizar el stock de un producto.
        El cambio puede ser positivo (añadir stock) o negativo (reducir stock).
        """
        producto_id = task_data.get("producto_id")
        cambio_stock = int(task_data.get("cambio", 0))

        if not producto_id or producto_id not in PRODUCTOS_DB:
            return {"status": "FAILED", "error": f"Producto con ID '{producto_id}' no encontrado."}

        stock_actual = PRODUCTOS_DB[producto_id]["stock_disponible"]
        nuevo_stock = stock_actual + cambio_stock

        if nuevo_stock < 0:
            return {"status": "FAILED", "error": f"No se puede reducir el stock a un valor negativo. Stock actual: {stock_actual}"}

        print(f"CAPITAN INVENTARIO: Actualizando stock para '{producto_id}'. De {stock_actual} a {nuevo_stock}.")
        PRODUCTOS_DB[producto_id]["stock_disponible"] = nuevo_stock

        return {
            "status": "COMPLETED",
            "result": {"producto_id": producto_id, "nuevo_stock": nuevo_stock, "mensaje": "Stock actualizado."}
        }

    def _handle_consultar_disponibilidad(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Lógica para consultar la información y disponibilidad de un producto.
        """
        producto_id = task_data.get("producto_id")

        if not producto_id or producto_id not in PRODUCTOS_DB:
            return {"status": "FAILED", "error": f"Producto con ID '{producto_id}' no encontrado."}

        print(f"CAPITAN INVENTARIO: Consultando disponibilidad del producto '{producto_id}'.")
        return {
            "status": "COMPLETED",
            "result": {"producto_data": PRODUCTOS_DB[producto_id]}
        }

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Maneja tareas desconocidas para este capitán."""
        task_type = task_data.get("type")
        return {
            "status": "FAILED",
            "error": f"El CapitanInventarioProductos no puede manejar la tarea de tipo '{task_type}'."
        }

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanInventarioProductos()

    # 1. Crear un producto
    tarea_crear = {
        "type": "crear_producto",
        "datos_producto": {"nombre": "Tour a la Cascada", "precio": 75.50, "stock_disponible": 20}
    }
    resultado_crear = capitan.execute_task(tarea_crear)
    print("Resultado Crear:", resultado_crear)

    print("\nBD de Productos:", PRODUCTOS_DB)
    print("-" * 20)

    # 2. Actualizar stock (simulando una reserva)
    producto_id = resultado_crear.get("result", {}).get("producto_id")
    tarea_actualizar = {
        "type": "actualizar_stock",
        "producto_id": producto_id,
        "cambio": -5
    }
    resultado_actualizar = capitan.execute_task(tarea_actualizar)
    print("Resultado Actualizar:", resultado_actualizar)
    print("-" * 20)

    # 3. Consultar disponibilidad
    tarea_consultar = {"type": "consultar_disponibilidad", "producto_id": producto_id}
    resultado_consultar = capitan.execute_task(tarea_consultar)
    print("Resultado Consultar:", resultado_consultar)
