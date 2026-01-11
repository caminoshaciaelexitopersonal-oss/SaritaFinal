"""
Módulo de Descomposición de Tareas Tácticas para SG-SST.

Este componente toma una fase del plan estratégico (del Planner) y la
descompone en un conjunto de tareas atómicas y específicas que pueden ser
asignadas a los Capitanes para su ejecución.
"""

from typing import Dict, Any, List

class SSTTaskDecomposer:
    """
    Convierte fases estratégicas en tareas tácticas ejecutables.
    """

    def __init__(self, policies):
        """
        Inicializa el descomponedor con las políticas del dominio.

        Args:
            policies: Una instancia de SSTPolicies para consultar normativas.
        """
        self.policies = policies
        print("DECOMPOSER: Descomponedor de Tareas SG-SST inicializado.")

    def decompose_phase(self, phase: str, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Descompone una fase del plan en tareas tácticas.

        Args:
            phase (str): La fase del plan a descomponer (ej. "fase_2_inspeccion_instalaciones").
            context (Dict[str, Any]): Contexto de la orden, puede incluir detalles del objetivo.

        Returns:
            List[Dict[str, Any]]: Una lista de diccionarios, donde cada uno es una tarea táctica.
                                  Devuelve una lista vacía si la fase no es reconocida.
        """
        target_id = context.get("target_id", "unknown_target")
        print(f"DECOMPOSER: Descomponiendo fase '{phase}' para el objetivo '{target_id}'.")

        # Usamos un "despachador" para llamar al método de descomposición correcto.
        decomposer_method = getattr(self, f"_decompose_{phase}", self._decompose_default)
        return decomposer_method(context)

    def _decompose_fase_1_recoleccion_documental(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Descompone la fase de recolección de documentos."""
        print("DECOMPOSER: Aplicando lógica de descomposición para 'Recolección Documental'.")
        tasks = [
            {"type": "solicitar_documento", "documento": "matriz_riesgos_actualizada", "capitan_requerido": "documentacion"},
            {"type": "solicitar_documento", "documento": "registros_capacitacion_brigada", "capitan_requerido": "documentacion"},
            {"type": "verificar_vencimiento", "documento": "certificados_fumigacion", "dias_max_vencido": 365, "capitan_requerido": "verificacion"},
        ]
        return tasks

    def _decompose_fase_2_inspeccion_instalaciones(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Descompone la fase de inspección de instalaciones."""
        print("DECOMPOSER: Aplicando lógica de descomposición para 'Inspección de Instalaciones'.")
        # Simulación: podría obtener las áreas a inspeccionar de una base de datos o del contexto.
        areas_a_inspeccionar = ["recepcion", "cocina", "piso_1_habitaciones", "areas_comunes"]
        tasks = []
        for area in areas_a_inspeccionar:
            tasks.append({"type": "inspeccionar_area", "area": area, "checklist": "general_seguridad", "capitan_requerido": "inspeccion_campo"})

        # Añadir tareas específicas basadas en políticas
        freq_extintores = self.policies.FRECUENCIA_INSPECCION_EXTINTORES_DIAS
        tasks.append({"type": "verificar_equipo", "equipo": "extintores", "frecuencia_dias": freq_extintores, "capitan_requerido": "inspeccion_equipos"})

        return tasks

    def _decompose_default(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Método por defecto si no se encuentra una descomposición específica."""
        phase = context.get('current_phase', 'desconocida')
        print(f"DECOMPOSER: Advertencia - No hay lógica de descomposición específica para la fase '{phase}'.")
        return [{"type": "generica", "details": f"Tarea genérica para la fase {phase}", "capitan_requerido": "default"}]

# Ejemplo de uso
if __name__ == '__main__':
    from policies import SSTPolicies

    # 1. Instanciar el descomponedor con las políticas
    decomposer = SSTTaskDecomposer(policies=SSTPolicies())

    # 2. Definir una fase y un contexto
    fase_a_descomponer = "fase_2_inspeccion_instalaciones"
    orden_contexto = {"target_id": "hotel_principal", "current_phase": fase_a_descomponer}

    # 3. Descomponer la fase en tareas
    tareas_generadas = decomposer.decompose_phase(fase_a_descomponer, orden_contexto)

    print(f"\n--- Tareas Tácticas Generadas para '{fase_a_descomponer}' ---")
    if tareas_generadas:
        for i, tarea in enumerate(tareas_generadas, 1):
            print(f"  {i}. {tarea}")
    else:
        print("No se generaron tareas.")
    print("----------------------------------------------------------")
