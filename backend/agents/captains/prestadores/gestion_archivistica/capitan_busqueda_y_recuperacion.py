"""
Agente Capitán Táctico: CapitanBusquedaYRecuperacion

Responsable de ejecutar tareas atómicas de búsqueda y recuperación
de documentos basado en diversos criterios.
"""

from typing import Dict, Any, List

# --- Simulación de Dependencias (Base de Datos de otro Capitán) ---

# Base de datos simulada de documentos (de CapitanClasificacionDocumental)
DOCUMENTOS_DB = {
    "DOC-1111": {"id": "DOC-1111", "nombre_archivo": "contrato_cliente_A.pdf", "categoria": "Legal", "metadatos": {"cliente_id": "CLI-123", "tipo_archivo": "pdf"}},
    "DOC-2222": {"id": "DOC-2222", "nombre_archivo": "poliza_seguro_vehiculo.pdf", "categoria": "Seguros", "metadatos": {"vehiculo_id": "VEH-456", "tipo_archivo": "pdf"}},
    "DOC-3333": {"id": "DOC-3333", "nombre_archivo": "factura_venta_001.xml", "categoria": "Financiero", "metadatos": {"cliente_id": "CLI-123", "factura_id": "FV-001"}}
}

# --- Fin de Simulación ---

class CapitanBusquedaYRecuperacion:
    """
    Ejecuta tareas tácticas de búsqueda y recuperación documental.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task_payload.get("type")
        print(f"CAPITAN BUSQUEDA: Recibida tarea táctica '{task_type}'.")
        handler = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler(task_payload)

    def _handle_buscar_documentos_por_metadatos(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Busca documentos que coincidan con un conjunto de criterios en sus metadatos.
        """
        criterios = task_data.get("criterios", {})
        if not criterios:
            return {"status": "FAILED", "error": "Se requieren criterios de búsqueda."}

        print(f"CAPITAN BUSQUEDA: Buscando documentos con criterios: {criterios}")

        resultados = []
        for doc_id, doc_data in DOCUMENTOS_DB.items():
            coincide = True
            for clave, valor in criterios.items():
                if clave == "categoria" and doc_data.get("categoria") != valor:
                    coincide = False
                    break
                if doc_data.get("metadatos", {}).get(clave) != valor:
                    coincide = False
                    break
            if coincide:
                # Devolvemos una versión resumida en la búsqueda
                resultados.append({"id": doc_id, "nombre_archivo": doc_data["nombre_archivo"], "categoria": doc_data["categoria"]})

        return {"status": "COMPLETED", "result": {"documentos_encontrados": resultados}}

    def _handle_recuperar_documento_por_id(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recupera toda la información de un documento específico por su ID.
        """
        documento_id = task_data.get("documento_id")
        if not documento_id or documento_id not in DOCUMENTOS_DB:
            return {"status": "FAILED", "error": f"Documento con ID '{documento_id}' no encontrado."}

        print(f"CAPITAN BUSQUEDA: Recuperando documento completo con ID '{documento_id}'.")

        # En un sistema real, aquí se obtendría el contenido desde S3 o similar.
        documento_completo = DOCUMENTOS_DB[documento_id]
        documento_completo["contenido_b64_simulado"] = "SGFsbG8gV2VsdCE="

        return {"status": "COMPLETED", "result": {"documento": documento_completo}}

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "FAILED", "error": "Tarea de búsqueda o recuperación desconocida."}

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanBusquedaYRecuperacion()

    print("--- Caso 1: Búsqueda por metadatos (cliente_id) ---")
    tarea1 = {"type": "buscar_documentos_por_metadatos", "criterios": {"cliente_id": "CLI-123"}}
    resultado1 = capitan.execute_task(tarea1)
    print("Resultado Búsqueda 1:", resultado1)
    print("-" * 20)

    print("\n--- Caso 2: Búsqueda por categoría y tipo de archivo ---")
    tarea2 = {"type": "buscar_documentos_por_metadatos", "criterios": {"categoria": "Seguros", "tipo_archivo": "pdf"}}
    resultado2 = capitan.execute_task(tarea2)
    print("Resultado Búsqueda 2:", resultado2)
    print("-" * 20)

    print("\n--- Caso 3: Recuperar un documento por ID ---")
    tarea3 = {"type": "recuperar_documento_por_id", "documento_id": "DOC-1111"}
    resultado3 = capitan.execute_task(tarea3)
    print("Resultado Recuperación:", resultado3)
    print("-" * 20)
