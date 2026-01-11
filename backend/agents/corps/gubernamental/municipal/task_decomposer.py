"""
Módulo de Descomposición de Tareas Tácticas para Gobernanza Municipal.

Este componente toma una fase del plan estratégico y la descompone en tareas
atómicas y específicas para los Capitanes del dominio municipal.
"""

from typing import Dict, Any, List

class GubernamentalMunicipalTaskDecomposer:
    """
    Convierte fases estratégicas municipales en tareas tácticas ejecutables.
    """

    def __init__(self, policies):
        """
        Inicializa el descomponedor con las políticas del dominio.
        """
        self.policies = policies
        print("DECOMPOSER: Descomponedor de Tareas Gubernamental Municipal inicializado.")

    def decompose_phase(self, phase: str, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Descompone una fase del plan en tareas tácticas.
        """
        solicitud_id = context.get("solicitud_id", "unknown_id")
        print(f"DECOMPOSER: Descomponiendo fase '{phase}' para la solicitud '{solicitud_id}'.")

        decomposer_method = getattr(self, f"_decompose_{phase}", self._decompose_default)
        return decomposer_method(context)

    def _decompose_fase_1_recepcion_documental(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Descompone la fase de recepción de documentos para una licencia."""
        documentos_requeridos = ["camara_comercio", "uso_de_suelo", "certificado_bomberos"]
        tasks = []
        for doc in documentos_requeridos:
            tasks.append({"type": "verificar_documento_adjunto", "documento": doc, "capitan_requerido": "validacion_documental"})
        return tasks

    def _decompose_fase_2_validacion_requisitos_legales(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Descompone la fase de validación de requisitos legales."""
        tasks = [
            {"type": "consultar_antecedentes_judiciales", "identificacion": context.get("solicitante_id"), "capitan_requerido": "consulta_externa"},
            {"type": "verificar_pago_impuestos_municipales", "nit": context.get("nit_establecimiento"), "capitan_requerido": "consulta_financiera_interna"},
        ]
        return tasks

    def _decompose_fase_3_inspeccion_fisica(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Descompone la fase de inspección física."""
        tasks = [
            {"type": "agendar_visita_inspeccion", "direccion": context.get("direccion"), "capitan_requerido": "logistica"},
            {"type": "ejecutar_checklist_inspeccion", "tipo_checklist": "sanitario_y_seguridad", "direccion": context.get("direccion"), "capitan_requerido": "inspeccion_campo"},
        ]
        return tasks

    def _decompose_default(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Método por defecto si no se encuentra una descomposición específica."""
        phase = context.get('current_phase', 'desconocida')
        return [{"type": "generica", "details": f"Tarea para la fase {phase}", "capitan_requerido": "default"}]

# Ejemplo de uso
if __name__ == '__main__':
    from policies import GubernamentalMunicipalPolicies

    decomposer = GubernamentalMunicipalTaskDecomposer(policies=GubernamentalMunicipalPolicies())

    fase_a_descomponer = "fase_2_validacion_requisitos_legales"
    orden_contexto = {"solicitud_id": "LIC-2024-001", "solicitante_id": "12345678", "nit_establecimiento": "987654321"}

    tareas = decomposer.decompose_phase(fase_a_descomponer, orden_contexto)

    print(f"\n--- Tareas para '{fase_a_descomponer}' ---")
    for i, tarea in enumerate(tareas, 1):
        print(f"  {i}. {tarea}")
