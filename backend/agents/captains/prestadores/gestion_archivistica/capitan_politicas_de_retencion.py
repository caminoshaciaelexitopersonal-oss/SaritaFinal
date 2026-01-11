"""
Agente Capitán Táctico: CapitanPoliticasDeRetencion

Responsable de aplicar políticas de ciclo de vida a los documentos,
como el archivado a largo plazo, la revisión o la eliminación segura.
"""

from typing import Dict, Any
from datetime import datetime, timedelta

# --- Simulación de Dependencias (Base de Datos de otro Capitán) ---

# Base de datos simulada de documentos
DOCUMENTOS_DB = {
    "DOC-1111": {
        "id": "DOC-1111", "categoria": "Legal", "estado": "ACTIVO",
        "timestamp_creacion": (datetime.utcnow() - timedelta(days=2000)).isoformat() # Muy antiguo
    },
    "DOC-2222": {
        "id": "DOC-2222", "categoria": "Financiero", "estado": "ACTIVO",
        "timestamp_creacion": (datetime.utcnow() - timedelta(days=100)).isoformat() # Reciente
    },
    "DOC-3333": {
        "id": "DOC-3333", "categoria": "Legal", "estado": "ACTIVO",
        "timestamp_creacion": (datetime.utcnow() - timedelta(days=4000)).isoformat() # Muy muy antiguo
    }
}

# --- Fin de Simulación ---

class CapitanPoliticasDeRetencion:
    """
    Ejecuta tareas tácticas de ciclo de vida y políticas de retención.
    """

    # Políticas de retención (en días)
    POLITICAS = {
        "Legal": {"archivar_despues_de": 1825, "eliminar_despues_de": 3650}, # 5 y 10 años
        "Financiero": {"archivar_despues_de": 1095, "eliminar_despues_de": 2555}, # 3 y 7 años
        "Default": {"archivar_despues_de": 730, "eliminar_despues_de": 1825} # 2 y 5 años
    }

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task_payload.get("type")
        print(f"CAPITAN RETENCION: Recibida tarea táctica '{task_type}'.")
        handler = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler(task_payload)

    def _handle_ejecutar_ciclo_de_vida(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recorre todos los documentos y aplica las políticas de retención.
        """
        print(f"CAPITAN RETENCION: Iniciando ciclo de vida para {len(DOCUMENTOS_DB)} documentos.")

        archivados = 0
        eliminados = 0
        ahora = datetime.utcnow()

        # Usamos list(keys()) para poder modificar el diccionario mientras iteramos
        for doc_id in list(DOCUMENTOS_DB.keys()):
            doc = DOCUMENTOS_DB[doc_id]
            if doc.get("estado") != "ACTIVO":
                continue

            politica = self.POLITICAS.get(doc["categoria"], self.POLITICAS["Default"])
            fecha_creacion = datetime.fromisoformat(doc["timestamp_creacion"])
            antiguedad_dias = (ahora - fecha_creacion).days

            if antiguedad_dias > politica["eliminar_despues_de"]:
                print(f"  -> Eliminando documento '{doc_id}' (antigüedad: {antiguedad_dias} días).")
                del DOCUMENTOS_DB[doc_id]
                eliminados += 1
            elif antiguedad_dias > politica["archivar_despues_de"]:
                print(f"  -> Archivando documento '{doc_id}' (antigüedad: {antiguedad_dias} días).")
                doc["estado"] = "ARCHIVADO"
                archivados += 1

        return {
            "status": "COMPLETED",
            "result": {"documentos_archivados": archivados, "documentos_eliminados": eliminados}
        }

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "FAILED", "error": "Tarea de retención desconocida."}

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanPoliticasDeRetencion()

    print("--- Estado Inicial de la Base de Datos ---")
    print(DOCUMENTOS_DB)
    print("-" * 20)

    print("\n--- Ejecutando Ciclo de Vida ---")
    tarea = {"type": "ejecutar_ciclo_de_vida"}
    resultado = capitan.execute_task(tarea)
    print("Resultado del ciclo:", resultado)
    print("-" * 20)

    print("\n--- Estado Final de la Base de Datos ---")
    print(DOCUMENTOS_DB)
    print("-" * 20)

    # Verificamos que DOC-1111 está archivado y DOC-3333 eliminado
    assert DOCUMENTOS_DB["DOC-1111"]["estado"] == "ARCHIVADO"
    assert "DOC-3333" not in DOCUMENTOS_DB
    assert DOCUMENTOS_DB["DOC-2222"]["estado"] == "ACTIVO"
    print("Verificaciones automáticas correctas.")
