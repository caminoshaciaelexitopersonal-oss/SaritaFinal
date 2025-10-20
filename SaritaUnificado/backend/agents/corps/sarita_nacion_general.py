# -*- coding: utf-8 -*-
import json
from typing import TypedDict, List, Any, Dict
# from langchain_core.pydantic_v1 import BaseModel, Field
import functools
from langgraph.graph import StateGraph, END
from ai_models.llm_router import route_llm_request
from .sarita_departamento_general import get_sarita_departamento_graph
import logging

logger = logging.getLogger(__name__)

# --- DEFINICIÓN DEL ESTADO Y EL PLAN ESTRATÉGICO DEL GENERAL DE LA NACIÓN ---

class DepartmentalDirective(BaseModel):
    """Define una directiva estratégica para ser asignada a un General de Departamento."""
    directive_description: str = Field(description="La descripción detallada de la directiva para el General de Departamento.")
    responsible_department: str = Field(description="El departamento a cargo. Por ahora, solo 'Meta' está disponible.")

class NationalPlan(BaseModel):
    """El plan estratégico nacional generado por SARITA Nación."""
    plan: List[DepartmentalDirective] = Field(description="La lista de directivas estratégicas para cumplir el mandato.")

class SaritaNacionState(TypedDict):
    """El estado del General de la Nación."""
    mandate: str
    user: Any  # Cambiado de user_id a user
    task_id: str
    conversation_history: List[Dict[str, str]]
    national_plan: NationalPlan | None
    task_queue: List[DepartmentalDirective]
    completed_directives: list
    final_report: str
    error: str | None

# --- PUESTO DE MANDO: INSTANCIACIÓN DE GENERALES DE DEPARTAMENTO ---
# En el futuro, esto podría cargarse dinámicamente según los departamentos disponibles.
department_generals = {
    "Meta": get_sarita_departamento_graph(),
}

# --- NODOS DEL GRAFO DE MANDO DEL GENERAL DE LA NACIÓN ---

async def create_national_plan(state: SaritaNacionState) -> SaritaNacionState:
    """(NODO 1: PLANIFICADOR NACIONAL) Analiza el mandato y lo descompone en un plan de acción para los Departamentos."""
    print(f"--- 🇨🇴 SARITA NACIÓN: Creando Plan Estratégico Nacional... ---")

    prompt = f"""
Eres SARITA, la IA General al mando de toda la red de agentes territoriales de Colombia.
Tu deber es analizar un mandato y descomponerlo en directivas claras para tus Generales de Departamento.
Actualmente, el único departamento operativo es 'Meta'. Todas las tareas deben ser asignadas a él.
Devuelve SIEMPRE una respuesta en formato JSON válido, siguiendo la estructura de la clase `NationalPlan`.

**Mandato: "{state['mandate']}"**
"""
    try:
        llm_response_str = await route_llm_request(prompt, state.get("conversation_history", []), state.get("user"))
        llm_response_json = json.loads(llm_response_str)
        plan = NationalPlan.parse_obj(llm_response_json)

        state.update({
            "national_plan": plan,
            "task_queue": plan.plan.copy(),
            "completed_directives": [],
            "error": None
        })
    except Exception as e:
        state["error"] = f"Error crítico al planificar a nivel nacional: {e}"
    return state

def route_to_department(state: SaritaNacionState):
    """(NODO 2: ENRUTADOR DE MANDO) Selecciona el Departamento según la próxima directiva."""
    if state.get("error") or not state.get("task_queue"):
        return "compile_report"

    next_directive = state["task_queue"][0]
    department_unit = next_directive.responsible_department

    if department_unit in department_generals:
        return department_unit
    else:
        state["error"] = f"Error de planificación: Departamento '{department_unit}' desconocido."
        state["task_queue"].pop(0)
        return "route_to_department"

async def delegate_directive_to_department(state: SaritaNacionState, department_name: str) -> SaritaNacionState:
    """(NODO DE DELEGACIÓN) Invoca al sub-grafo del General de Departamento adecuado."""
    directive = state["task_queue"].pop(0)
    print(f"--- 🔽 SARITA NACIÓN: Delegando a {department_name.upper()} -> '{directive.directive_description}' ---")
    try:
        department_agent = department_generals[department_name]

        result = await department_agent.ainvoke({
            "directive": directive.directive_description,
            "user": state["user"],
            "task_id": state["task_id"],
            "conversation_history": state.get("conversation_history", [])
        })

        state["completed_directives"].append({
            "department": department_name,
            "directive": directive.directive_description,
            "report": result.get("final_report", "Sin reporte.")
        })
    except Exception as e:
        state["error"] = f"Error al ejecutar General de Departamento {department_name}: {e}"
    return state

async def compile_final_report(state: SaritaNacionState) -> SaritaNacionState:
    """(NODO FINAL) Compila los reportes de todos los Departamentos."""
    print("--- 📄 SARITA NACIÓN: Compilando Informe Final para el usuario... ---")
    if state.get("error"):
        state["final_report"] = f"Mandato fallido. Razón: {state['error']}"
    else:
        report_body = "\n".join([
            f"- Reporte del Departamento de {m['department']}:\n  Directiva: '{m['directive']}'\n  Resultado: {m['report']}"
            for m in state["completed_directives"]
        ])
        state["final_report"] = f"Mandato completado con éxito.\nResumen de Operaciones:\n{report_body}"

    return state

def get_sarita_nacion_graph():
    """Construye y compila el agente LangGraph para SARITA Nación."""
    workflow = StateGraph(SaritaNacionState)

    workflow.add_node("planner", create_national_plan)
    workflow.add_node("router", lambda s: s)

    for name in department_generals.keys():
        # Usar functools.partial para crear una nueva función con el nombre del departamento ya establecido
        node_function = functools.partial(delegate_directive_to_department, department_name=name)
        workflow.add_node(name, node_function)
        workflow.add_edge(name, "router")

    workflow.add_node("compiler", compile_final_report)

    workflow.set_entry_point("planner")
    workflow.add_edge("planner", "router")

    conditional_map = {name: name for name in department_generals.keys()}
    conditional_map["compile_report"] = "compiler"
    workflow.add_conditional_edges("router", route_to_department, conditional_map)

    workflow.add_edge("compiler", END)

    print("🇨🇴 SARITA NACIÓN: Puesto de mando central establecido. Todos los sistemas operativos.")
    return workflow.compile()