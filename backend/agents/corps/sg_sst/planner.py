"""
Módulo de Planificación Estratégica para el Coronel SG-SST.

Este componente recibe el objetivo operativo del General y lo traduce en un
plan de ejecución de alto nivel, secuencial o paralelo, específico para
el dominio de Seguridad y Salud en el Trabajo.
"""

from typing import Dict, Any, List

class SSTPlanner:
    """
    Crea planes estratégicos para cumplir con las órdenes del dominio SG-SST.
    """

    def __init__(self, policies):
        """
        Inicializa el planificador con las políticas del dominio.

        Args:
            policies: Una instancia de SSTPolicies para consultar normativas.
        """
        self.policies = policies
        print("PLANNER: Planificador Estratégico SG-SST inicializado.")

    def create_plan(self, objective: Dict[str, Any]) -> List[str]:
        """
        Genera un plan estratégico basado en el objetivo de la orden.

        Args:
            objective (Dict[str, Any]): El objetivo extraído del comando del General.
                                       Ej: {'action': 'auditar', 'target': 'instalacion_hotel_principal'}

        Returns:
            List[str]: Una lista ordenada de fases que componen el plan estratégico.
                       Devuelve una lista vacía si el objetivo no es reconocido.
        """
        action = objective.get("action")
        target_type = objective.get("target_type", "default")

        print(f"PLANNER: Creando plan para la acción '{action}' sobre un objetivo tipo '{target_type}'.")

        # Lógica de enrutamiento para seleccionar la plantilla de plan correcta.
        if action == "realizar_auditoria_mensual":
            return self._plan_auditoria_completa(objective)
        elif action == "investigar_incidente":
            return self._plan_investigacion_incidente(objective)
        else:
            print(f"PLANNER: Advertencia - No se encontró una plantilla de plan para la acción '{action}'.")
            return []

    def _plan_auditoria_completa(self, objective: Dict[str, Any]) -> List[str]:
        """
        Genera las fases para una auditoría de seguridad completa.
        """
        print("PLANNER: Usando plantilla de plan 'Auditoría Completa'.")
        # Aquí se podrían añadir fases condicionales basadas en las políticas.
        # Por ejemplo, si la instalación es de alto riesgo, añadir una fase de "validación externa".

        plan = [
            "fase_1_recoleccion_documental",
            "fase_2_inspeccion_instalaciones",
            "fase_3_entrevistas_personal",
            "fase_4_verificacion_equipos_emergencia",
            "fase_5_consolidacion_hallazgos",
            "fase_6_generacion_reporte_preliminar",
            "fase_7_validacion_gerencial"
        ]
        print(f"PLANNER: Plan generado con {len(plan)} fases.")
        return plan

    def _plan_investigacion_incidente(self, objective: Dict[str, Any]) -> List[str]:
        """
        Genera las fases para la investigación de un incidente de seguridad.
        """
        print("PLANNER: Usando plantilla de plan 'Investigación de Incidente'.")
        plan = [
            "fase_1_aseguramiento_area",
            "fase_2_recoleccion_evidencia",
            "fase_3_entrevistas_testigos",
            "fase_4_analisis_causa_raiz",
            "fase_5_elaboracion_informe_final"
        ]
        print(f"PLANNER: Plan generado con {len(plan)} fases.")
        return plan

# Ejemplo de uso
if __name__ == '__main__':
    from policies import SSTPolicies

    # 1. Se instancia el planificador con las políticas
    sst_planner = SSTPlanner(policies=SSTPolicies())

    # 2. Se define un objetivo (simulando una orden del General)
    orden_auditoria = {
        "action": "realizar_auditoria_mensual",
        "target_type": "instalacion",
        "target_id": "hotel_principal"
    }

    # 3. Se crea el plan
    plan_generado = sst_planner.create_plan(orden_auditoria)

    print("\n--- Plan Estratégico Generado ---")
    if plan_generado:
        for i, fase in enumerate(plan_generado, 1):
            print(f"  {i}. {fase}")
    else:
        print("No se pudo generar un plan.")
    print("---------------------------------")
