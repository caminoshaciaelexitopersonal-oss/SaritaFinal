import json
from typing import TypedDict, List, Any, Dict
from langchain_core.pydantic_v1 import BaseModel, Field
import functools
from langgraph.graph import StateGraph, END
from ai_models.llm_router import route_llm_request

# --- Importamos a los comandantes de campo: los Capitanes ---
from .units.admin_captain import get_admin_captain_graph
from .units.funcionario_captain import get_funcionario_captain_graph
from .units.prestadores_captain import get_prestadores_captain_graph
from .units.artesanos_captain import get_artesanos_captain_graph
from .units.turista_captain import get_turista_captain_graph
from .units.publicaciones_captain import get_publicaciones_captain_graph
from .units.atractivos_captain import get_atractivos_captain_graph
from .units.oferta_captain import get_oferta_captain_graph
from .units.videos_captain import get_videos_captain_graph

# --- DEFINICIÓN DEL ESTADO Y EL PLAN TÁCTICO DEL CORONEL ---

class CaptainTask(BaseModel):
    """Define una misión táctica clara para ser asignada a un Capitán."""
    task_description: str = Field(description="La descripción específica y detallada de la misión para el Capitán.")
    responsible_captain: str = Field(description="El Capitán especialista. Debe ser uno de: 'Admin', 'Funcionario', 'Prestadores', 'Artesanos', 'Turista', 'Publicaciones', 'Atractivos', 'Oferta', 'Videos'.")

class TacticalPlan(BaseModel):
    """El plan táctico completo generado por el Coronel."""
    plan: List[CaptainTask] = Field(description="La lista de misiones tácticas secuenciales para cumplir la orden.")

class TurismoColonelState(TypedDict):
    """La pizarra táctica del Coronel de Turismo."""
    general_order: str
    app_context: Any
    conversation_history: List[Dict[str, str]]
    tactical_plan: TacticalPlan | None
    task_queue: List[CaptainTask]
    completed_missions: list
    final_report: str
    error: str | None

# --- PUESTO DE MANDO: INSTANCIACIÓN DE CAPITANES ---
# Se instancian una sola vez para eficiencia
capitanes = {
    "Admin": get_admin_captain_graph(),
    "Funcionario": get_funcionario_captain_graph(),
    "Prestadores": get_prestadores_captain_graph(),
    "Artesanos": get_artesanos_captain_graph(),
    "Turista": get_turista_captain_graph(),
    "Publicaciones": get_publicaciones_captain_graph(),
    "Atractivos": get_atractivos_captain_graph(),
    "Oferta": get_oferta_captain_graph(),
    "Videos": get_videos_captain_graph(),
}

# --- NODOS DEL GRAFO DE MANDO DEL CORONEL ---

async def create_tactical_plan(state: TurismoColonelState) -> TurismoColonelState:
    """(NODO 1: PLANIFICADOR TÁCTICO) Analiza la orden, la enruta al LLM adecuado y descompone el resultado en un plan de acción."""
    print(f"--- 🧠 CORONEL DE TURISMO: Creando Plan Táctico... ---")

    # Extraer el contexto del usuario para el enrutador LLM
    user_context = state.get("app_context", {})
    user = user_context.get("user")  # Se espera que el objeto de usuario esté aquí
    conversation_history = state.get("conversation_history", [])

    # El prompt ahora es una guía clara para el LLM sobre sus capacidades
    base_prompt = f"""
Eres el Coronel de la División de Turismo. Tu General (el usuario) te ha dado una orden estratégica.
Tu deber es analizar esta orden y descomponerla en un plan táctico, asignando cada misión al Capitán especialista más adecuado.
Debes devolver SIEMPRE una respuesta en formato JSON válido, siguiendo la estructura de la clase `TacticalPlan`.

**Capitanes bajo tu mando y sus especialidades:**
- **'Admin'**: Capitán de administración general. Asigna misiones de configuración del sitio, gestión de usuarios y moderación de alto nivel.
- **'Funcionario'**: Capitán del cuerpo de funcionarios. Asigna misiones de gestión de contenido institucional, creación de plantillas de verificación y ejecución de verificaciones de campo.
- **'Prestadores'**: Capitán para el rol de Prestador. Asigna misiones para que los prestadores gestionen sus propios perfiles (actualizar datos, fotos, etc.).
- **'Artesanos'**: Capitán para el rol de Artesano. Asigna misiones para que los artesanos gestionen sus perfiles.
- **'Turista'**: Capitán de asistencia al turista. Asigna misiones de búsqueda de información, planificación de viajes y envío de reseñas.
- **'Publicaciones'**: Capitán de contenido. Asigna misiones para crear o gestionar noticias, blogs y eventos.
- **'Atractivos'**: Capitán de inventario. Asigna misiones para crear o gestionar los atractivos turísticos.
- **'Oferta'**: Capitán de oferta comercial. Asigna misiones para crear y gestionar rutas turísticas.
- **'Videos'**: Capitán de contenido audiovisual. Asigna misiones para gestionar la sección de videos.
"""

    # Doctrina especial para usuarios no registrados (invitados)
    guest_protocol = ""
    is_guest = not user or not user.is_authenticated
    if is_guest:
        guest_protocol = """

**PROTOCOLO PARA VISITANTES (NO REGISTRADOS):**
Tu misión tiene tres fases, en este orden exacto:
1.  **Identificar Origen:** Tu primera tarea es conversar con el usuario para identificar su origen. Debes preguntarle amablemente si es de Puerto Gaitán (Local), de otro municipio del Meta (Regional), de otra parte de Colombia (Nacional) o de otro país (Extranjero). Usa al Capitán Turista para esta interacción.
2.  **Responder y Guiar:** Una vez que tengas su origen, responde a su pregunta principal usando al Capitán Turista para buscar información.
3.  **Invitar al Registro:** Finalmente, invítale cordialmente a registrarse en la plataforma para obtener una experiencia completa y personalizada, mencionando que podrá guardar sus lugares favoritos y recibir recomendaciones.
"""

    prompt = f"""
{base_prompt}
{guest_protocol}

Analiza la siguiente orden y genera el plan táctico en formato JSON. Sé conciso y directo en las descripciones de las tareas.
**Orden: "{state['general_order']}"**
"""
    try:
        # --- INVOCACIÓN DEL ROUTER HÍBRIDO ---
        llm_response_str = await route_llm_request(prompt, conversation_history, user)

        # Parsear la respuesta JSON del LLM
        llm_response_json = json.loads(llm_response_str)

        # Validar y estructurar con Pydantic
        plan = TacticalPlan.parse_obj(llm_response_json)

        state.update({
            "tactical_plan": plan,
            "task_queue": plan.plan.copy(),
            "completed_missions": [],
            "error": None
        })
    except json.JSONDecodeError as e:
        state["error"] = f"Error crítico: El LLM devolvió un JSON inválido. Respuesta: '{llm_response_str}'. Error: {e}"
    except Exception as e:
        state["error"] = f"Error crítico al planificar: {e}"
    return state

def route_to_captain(state: TurismoColonelState):
    """(NODO 2: ENRUTADOR DE MANDO) Selecciona el Capitán según la próxima misión."""
    if state.get("error") or not state.get("task_queue"):
        return "compile_report"

    next_mission = state["task_queue"][0]
    captain_unit = next_mission.responsible_captain

    if captain_unit in capitanes:
        return captain_unit
    else:
        state["error"] = f"Error de planificación: Capitán '{captain_unit}' desconocido."
        state["task_queue"].pop(0)
        return "route_to_captain"

async def delegate_mission(state: TurismoColonelState, captain_name: str) -> TurismoColonelState:
    """(NODO DE DELEGACIÓN) Invoca dinámicamente el sub-grafo del Capitán adecuado."""
    mission = state["task_queue"].pop(0)
    print(f"--- 🔽 CORONEL: Delegando a CAP. {captain_name.upper()} -> '{mission.task_description}' ---")
    try:
        captain_agent = capitanes[captain_name]
        # CORRECCIÓN VITAL: Pasar el app_context al capitán.
        result = await captain_agent.ainvoke({
            "coronel_order": mission.task_description,
            "app_context": state.get("app_context")
        })
        state["completed_missions"].append({
            "captain": captain_name,
            "mission": mission.task_description,
            "report": result.get("final_report", "Sin reporte.")
        })
    except Exception as e:
        state["error"] = f"Error al ejecutar Capitán {captain_name}: {e}"
    return state

async def compile_final_report(state: TurismoColonelState) -> TurismoColonelState:
    """(NODO FINAL) Compila los reportes de todos los Capitanes."""
    print("--- 📄 CORONEL DE TURISMO: Compilando Informe de División para el General... ---")
    if state.get("error"):
        state["final_report"] = f"Misión de la División fallida. Razón: {state['error']}"
    else:
        report_body = "\n".join([
            f"- Reporte del Capitán de {m['captain']}:\n  Misión: '{m['mission']}'\n  Resultado: {m['report']}"
            for m in state["completed_missions"]
        ])
        state["final_report"] = f"Misión de la División de Turismo completada.\nResumen de Operaciones:\n{report_body}"

    # Actualizar el historial de conversación para la próxima ronda
    history = state.get("conversation_history", [])
    history.append({"role": "user", "content": state["general_order"]})
    history.append({"role": "assistant", "content": state["final_report"]})
    state["conversation_history"] = history

    return state

# --- ENSAMBLAJE DEL GRAFO DE MANDO DEL CORONEL ---

def get_turismo_coronel_graph():
    """Construye y compila el agente LangGraph para el Coronel de Turismo."""
    workflow = StateGraph(TurismoColonelState)

    workflow.add_node("planner", create_tactical_plan)
    workflow.add_node("router", lambda s: s) # Nodo 'passthrough' para el enrutador

    for name in capitanes.keys():
        node_function = functools.partial(delegate_mission, captain_name=name)
        workflow.add_node(name, node_function)
        workflow.add_edge(name, "router")

    workflow.add_node("compiler", compile_final_report)

    workflow.set_entry_point("planner")
    workflow.add_edge("planner", "router")

    conditional_map = {name: name for name in capitanes.keys()}
    conditional_map["compile_report"] = "compiler"
    workflow.add_conditional_edges("router", route_to_captain, conditional_map)

    workflow.add_edge("compiler", END)

    print("⚜️ CORONEL DE TURISMO: Puesto de mando establecido. Ejército de agentes listo para recibir órdenes.")
    return workflow.compile()