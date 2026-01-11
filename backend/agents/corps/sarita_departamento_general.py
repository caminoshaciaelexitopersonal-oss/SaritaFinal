# -*- coding: utf-8 -*-
import json
from typing import TypedDict, List, Any, Dict
# from langchain_core.pydantic_v1 import BaseModel, Field
import functools
from langgraph.graph import StateGraph, END
from ai_models.llm_router import route_llm_request
from .turismo_coronel import get_turismo_coronel_graph
import logging

logger = logging.getLogger(__name__)

# --- DEFINICIÓN DEL ESTADO Y EL PLAN TÁCTICO DEL GENERAL DE DEPARTAMENTO ---

class ColonelTask(BaseModel):
    """Define una orden estratégica para ser asignada a un Coronel."""
    task_description: str = Field(description="La descripción detallada de la orden para el Coronel.")
    responsible_colonel: str = Field(description="El Coronel a cargo. Por ahora, solo 'TurismoCoronel' está disponible.")

class DepartmentalPlan(BaseModel):
    """El plan estratégico completo generado por el General de Departamento."""
    plan: List[ColonelTask] = Field(description="La lista de órdenes estratégicas para cumplir la directiva.")

class SaritaDepartamentoState(TypedDict):
    """El estado del General de Departamento."""
    directive: str
    user: Any # Cambiado de user_id a user
    task_id: str
    conversation_history: List[Dict[str, str]]
    strategic_plan: DepartmentalPlan | None
    task_queue: List[ColonelTask]
    completed_missions: list
    final_report: str
    error: str | None

# --- PUESTO DE MANDO: INSTANCIACIÓN DE CORONELES ---
coroneles = {
    "TurismoCoronel": get_turismo_coronel_graph(),
}

# --- NODOS DEL GRAFO DE MANDO DEL GENERAL DE DEPARTAMENTO ---

async def create_strategic_plan(state: SaritaDepartamentoState) -> SaritaDepartamentoState:
    """(NODO 1: PLANIFICADOR ESTRATÉGICO) Analiza la directiva y la descompone en un plan de acción para los Coroneles."""
    print(f"--- 🏛️ GENERAL DE DEPARTAMENTO: Creando Plan Estratégico... ---")

    prompt = f"""
Eres un General de Departamento en el sistema SARITA. Has recibido una directiva.
Tu deber es analizarla y descomponerla en órdenes claras para tus Coroneles.
Actualmente, solo tienes un Coronel bajo tu mando: 'TurismoCoronel', que se especializa en todas las tareas relacionadas con el turismo.
Devuelve SIEMPRE una respuesta en formato JSON válido, siguiendo la estructura de la clase `DepartmentalPlan`.

**Directiva: "{state['directive']}"**
"""
    try:
        llm_response_str = await route_llm_request(prompt, state.get("conversation_history", []), state.get("user"))
        llm_response_json = json.loads(llm_response_str)
        plan = DepartmentalPlan.parse_obj(llm_response_json)

        state.update({
            "strategic_plan": plan,
            "task_queue": plan.plan.copy(),
            "completed_missions": [],
            "error": None
        })
    except Exception as e:
        state["error"] = f"Error crítico al planificar: {e}"
    return state

def route_to_colonel(state: SaritaDepartamentoState):
    """(NODO 2: ENRUTADOR DE MANDO) Selecciona el Coronel según la próxima orden."""
    if state.get("error") or not state.get("task_queue"):
        return "compile_report"

    next_order = state["task_queue"][0]
    colonel_unit = next_order.responsible_colonel

    if colonel_unit in coroneles:
        return colonel_unit
    else:
        state["error"] = f"Error de planificación: Coronel '{colonel_unit}' desconocido."
        state["task_queue"].pop(0)
        return "route_to_colonel"

async def delegate_order_to_colonel(state: SaritaDepartamentoState, colonel_name: str) -> SaritaDepartamentoState:
    """(NODO DE DELEGACIÓN) Invoca al sub-grafo del Coronel adecuado."""
    order = state["task_queue"].pop(0)
    print(f"--- 🔽 GENERAL DE DEPARTAMENTO: Delegando a {colonel_name.upper()} -> '{order.task_description}' ---")
    try:
        colonel_agent = coroneles[colonel_name]
        # El app_context ahora pasa el objeto de usuario completo
        app_context = {"user": state["user"], "task_id": state["task_id"]}

        result = await colonel_agent.ainvoke({
            "general_order": order.task_description,
            "app_context": app_context,
            "conversation_history": state.get("conversation_history", [])
        })

        state["completed_missions"].append({
            "colonel": colonel_name,
            "order": order.task_description,
            "report": result.get("final_report", "Sin reporte.")
        })
    except Exception as e:
        state["error"] = f"Error al ejecutar Coronel {colonel_name}: {e}"
    return state

async def compile_final_report(state: SaritaDepartamentoState) -> SaritaDepartamentoState:
    """(NODO FINAL) Compila los reportes de todos los Coroneles."""
    print("--- 📄 GENERAL DE DEPARTAMENTO: Compilando Informe para el General de la Nación... ---")
    if state.get("error"):
        state["final_report"] = f"Directiva Departamental fallida. Razón: {state['error']}"
    else:
        report_body = "\n".join([
            f"- Reporte del {m['colonel']}:\n  Orden: '{m['order']}'\n  Resultado: {m['report']}"
            for m in state["completed_missions"]
        ])
        state["final_report"] = f"Directiva Departamental completada.\nResumen de Operaciones:\n{report_body}"

    return state

def get_sarita_departamento_graph():
    """Construye y compila el agente LangGraph para el General de Departamento."""
    workflow = StateGraph(SaritaDepartamentoState)

    workflow.add_node("planner", create_strategic_plan)
    workflow.add_node("router", lambda s: s)

    for name in coroneles.keys():
        node_function = functools.partial(delegate_order_to_colonel, colonel_name=name)
        workflow.add_node(name, node_function)
        workflow.add_edge(name, "router")

    workflow.add_node("compiler", compile_final_report)

    workflow.set_entry_point("planner")
    workflow.add_edge("planner", "router")

    conditional_map = {name: name for name in coroneles.keys()}
    conditional_map["compile_report"] = "compiler"
    workflow.add_conditional_edges("router", route_to_colonel, conditional_map)

    workflow.add_edge("compiler", END)

    print("🏛️ GENERAL DE DEPARTAMENTO: Puesto de mando establecido. Unidades de Coroneles listas.")
    return workflow.compile()