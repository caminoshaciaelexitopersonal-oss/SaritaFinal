"""
Módulo de Planificación Estratégica para el Coronel Gubernamental Municipal.

Este componente traduce los objetivos de gobernanza municipal en planes de alto nivel.
"""

from typing import Dict, Any, List

class GubernamentalMunicipalPlanner:
    """
    Crea planes estratégicos para órdenes del dominio Gubernamental Municipal.
    """

    def __init__(self, policies):
        """
        Inicializa el planificador con las políticas del dominio.
        """
        self.policies = policies
        print("PLANNER: Planificador Estratégico Gubernamental Municipal inicializado.")

    def create_plan(self, objective: Dict[str, Any]) -> List[str]:
        """
        Genera un plan estratégico basado en el objetivo de la orden.
        """
        action = objective.get("action")

        print(f"PLANNER: Creando plan para la acción '{action}'.")

        if action == "procesar_nueva_licencia":
            return self._plan_nueva_licencia(objective)
        elif action == "verificar_estado_establecimiento":
            return self._plan_verificacion_establecimiento(objective)
        else:
            print(f"PLANNER: Advertencia - No se encontró plantilla de plan para '{action}'.")
            return []

    def _plan_nueva_licencia(self, objective: Dict[str, Any]) -> List[str]:
        """
        Genera las fases para procesar una nueva licencia comercial.
        """
        print("PLANNER: Usando plantilla de plan 'Nueva Licencia Comercial'.")

        plan = [
            "fase_1_recepcion_documental",
            "fase_2_validacion_requisitos_legales"
        ]

        # Fase condicional basada en políticas
        actividad = objective.get("context", {}).get("actividad_comercial", "")
        if self.policies.requiere_inspeccion_para_actividad(actividad):
            plan.append("fase_3_inspeccion_fisica")
            print("PLANNER: Se añadió la fase de inspección física según las políticas.")

        plan.extend([
            "fase_4_emision_concepto",
            "fase_5_notificacion_solicitante"
        ])

        print(f"PLANNER: Plan generado con {len(plan)} fases.")
        return plan

    def _plan_verificacion_establecimiento(self, objective: Dict[str, Any]) -> List[str]:
        """
        Genera las fases para una verificación de rutina de un establecimiento.
        """
        print("PLANNER: Usando plantilla de plan 'Verificación de Establecimiento'.")
        return [
            "fase_1_consulta_estado_licencia",
            "fase_2_inspeccion_sanitaria_rutinaria",
            "fase_3_actualizacion_registro"
        ]

# Ejemplo de uso
if __name__ == '__main__':
    from policies import GubernamentalMunicipalPolicies

    planner = GubernamentalMunicipalPlanner(policies=GubernamentalMunicipalPolicies())

    orden_licencia_restaurante = {
        "action": "procesar_nueva_licencia",
        "context": {"actividad_comercial": "restaurante de comida rápida"}
    }

    plan_1 = planner.create_plan(orden_licencia_restaurante)

    print("\n--- Plan para Licencia de Restaurante ---")
    if plan_1:
        for i, fase in enumerate(plan_1, 1):
            print(f"  {i}. {fase}")

    print("\n" + "-"*20 + "\n")

    orden_licencia_oficina = {
        "action": "procesar_nueva_licencia",
        "context": {"actividad_comercial": "oficina de contabilidad"}
    }

    plan_2 = planner.create_plan(orden_licencia_oficina)

    print("--- Plan para Licencia de Oficina ---")
    if plan_2:
        for i, fase in enumerate(plan_2, 1):
            print(f"  {i}. {fase}")
