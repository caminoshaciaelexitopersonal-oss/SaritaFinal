"""
Agente Capitán Táctico: CapitanClasificacionDocumental

Responsable de ejecutar tareas atómicas relacionadas con la recepción,
clasificación y extracción de metadatos de documentos.
"""

from typing import Dict, Any
import uuid
from datetime import datetime
import base64

# Base de datos simulada de documentos
DOCUMENTOS_DB = {}

class CapitanClasificacionDocumental:
    """
    Ejecuta tareas tácticas de clasificación documental.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task_payload.get("type")
        print(f"CAPITAN DOCUMENTACION: Recibida tarea táctica '{task_type}'.")
        handler = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler(task_payload)

    def _handle_clasificar_nuevo_documento(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Procesa un nuevo documento, lo clasifica y extrae metadatos.
        """
        nombre_archivo = task_data.get("nombre_archivo")
        contenido_b64 = task_data.get("contenido_b64")
        categoria_sugerida = task_data.get("categoria", "General")

        if not nombre_archivo or not contenido_b64:
            return {"status": "FAILED", "error": "Nombre de archivo y contenido son requeridos."}

        print(f"CAPITAN DOCUMENTACION: Clasificando nuevo documento '{nombre_archivo}'.")

        # Simulación de extracción de metadatos y clasificación
        metadatos = self._extraer_metadatos(nombre_archivo, contenido_b64)
        categoria_final = self._determinar_categoria(nombre_archivo, metadatos, categoria_sugerida)

        doc_id = f"DOC-{uuid.uuid4().hex[:8].upper()}"
        DOCUMENTOS_DB[doc_id] = {
            "id": doc_id,
            "nombre_archivo": nombre_archivo,
            "categoria": categoria_final,
            "metadatos": metadatos,
            "version": 1,
            "timestamp_creacion": datetime.utcnow().isoformat(),
            # En un sistema real, el contenido podría ir a un S3 y aquí solo la URL.
            # Por simplicidad, no lo guardamos en la DB en memoria.
        }

        return {
            "status": "COMPLETED",
            "result": {"documento_id": doc_id, "categoria": categoria_final, "metadatos": metadatos}
        }

    def _extraer_metadatos(self, nombre_archivo: str, contenido_b64: str) -> Dict[str, Any]:
        """Simula la extracción de metadatos de un archivo."""
        try:
            # Simulación: calcular tamaño y tipo de archivo
            tamano_bytes = len(base64.b64decode(contenido_b64))
            tipo_archivo = nombre_archivo.split('.')[-1] if '.' in nombre_archivo else 'desconocido'

            return {
                "tamaño_bytes": tamano_bytes,
                "tipo_archivo": tipo_archivo.lower(),
                "analisis_contenido_simulado": "Contenido parece ser texto plano."
            }
        except Exception:
            return {"error": "Contenido Base64 inválido."}

    def _determinar_categoria(self, nombre_archivo: str, metadatos: Dict[str, Any], categoria_sugerida: str) -> str:
        """Simula una lógica de negocio para determinar la categoría final."""
        nombre_lower = nombre_archivo.lower()
        if "contrato" in nombre_lower:
            return "Legal"
        if "poliza" in nombre_lower or "seguro" in nombre_lower:
            return "Seguros"
        if metadatos.get("tipo_archivo") == "pdf":
            return "Documentos PDF"
        return categoria_sugerida

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "FAILED", "error": "Tarea de clasificación desconocida."}

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanClasificacionDocumental()

    # Simulación de un archivo de contrato en Base64
    contenido_contrato = base64.b64encode(b"Este es el contenido de un contrato de servicio.").decode('utf-8')

    print("--- Caso 1: Clasificar Contrato ---")
    tarea1 = {
        "type": "clasificar_nuevo_documento",
        "nombre_archivo": "Contrato_Prestacion_Servicios_2024.txt",
        "contenido_b64": contenido_contrato,
        "categoria": "Documentos Cliente" # Sugerencia inicial
    }
    resultado1 = capitan.execute_task(tarea1)
    print("Resultado:", resultado1)
    print("BD Documentos:", DOCUMENTOS_DB)
    print("-" * 20)

    # Simulación de un archivo de imagen
    contenido_imagen = base64.b64encode(b"fake_image_data").decode('utf-8')

    print("\n--- Caso 2: Clasificar Imagen JPG ---")
    tarea2 = {
        "type": "clasificar_nuevo_documento",
        "nombre_archivo": "logo_empresa.jpg",
        "contenido_b64": contenido_imagen,
        "categoria": "Marketing"
    }
    resultado2 = capitan.execute_task(tarea2)
    print("Resultado:", resultado2)
    print("-" * 20)
