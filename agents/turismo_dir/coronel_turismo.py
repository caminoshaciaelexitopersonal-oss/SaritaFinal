from typing import TypedDict, List
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver

# Stub captains (impl later)
def get_captain_graph(cap):
    return StateGraph({}).compile()  # stub

captains = {
    'admin': get_captain_graph('admin'),
    'dir_funcionarios': get_captain_graph('dir'),
    'prestadores': get_captain_graph('prestadores'),
    'artesanos': get_captain_graph('artesanos'),
    'turistas': get_captain_graph('turistas'),
    'videos': get_captain_graph('videos'),
    'oferta': get_captain_graph('oferta'),
    'atractivos': get_captain_graph('atractivos'),
    'blog': get_captain_graph('blog'),
}

llm = ChatOpenAI(model="gpt-4o", temperature=0, model_kwargs={"response_format": {"type": "json_object"}})

class TacticalTask(BaseModel):
    task_description: str = Field(description="Misión detallada para Captain.")
    responsible_captain: str = Field(description="Uno de: admin/dir/prestadores/artesanos/turistas/videos/oferta/atractivos/blog.")

class TacticalPlan(BaseModel):
    plan: List[TacticalTask]

class TurismoColonelState(TypedDict):
    general_order: str  # NL/voice
    tactical_plan: TacticalPlan | None
    task_queue: List[TacticalTask]
    completed_missions: list
    final_report: str
    error: str | None

async def create_tactical_plan(state):
    structured_llm = llm.with_structured_output(TacticalPlan)
    prompt = f"""Coronel Turismo DIR. Orden: "{state['general_order']}"
Capitanes: admin/dir_funcionarios/prestadores/artesanos/turistas/videos/oferta/atractivos/blog/noticias
Genera plan JSON."""
    plan = await structured_llm.ainvoke(prompt)
    return {'tactical_plan': plan, 'task_queue': plan.plan.copy()}

def route_to_captain(state):
    if not state['task_queue']: return 'compile_report'
    cap = state['task_queue'][0].responsible_captain
    return cap  # 'admin' etc.

# Stub captain nodes
async def captain_node(state, cap):
    mission = state['task_queue'].pop(0)
    result = await captains[cap].ainvoke({'coronel_order': mission.task_description})
    state['completed_missions'].append({'cap': cap, 'report': result['final_report']})
    return state

async def compile_report(state):
    state['final_report'] = 'Misión Turismo completada: ' + str(state['completed_missions'])
    return state

workflow = StateGraph(TurismoColonelState)
workflow.add_node('planner', create_tactical_plan)
workflow.add_node('router', lambda s: s)
for cap in captains:
    workflow.add_node(cap, lambda s, c=cap: captain_node(s, c))
workflow.add_node('compiler', compile_report)

workflow.set_entry_point('planner')
workflow.add_edge('planner', 'router')
workflow.add_conditional_edges('router', route_to_captain, {**captains, 'compile_report': 'compiler'})
for cap in captains:
    workflow.add_edge(cap, 'router')
workflow.add_edge('compiler', END)

memory = SqliteSaver.from_conn_string(":memory:")
app = workflow.compile(checkpointer=memory)

# Use: app.invoke({'general_order': 'Crea prestador hotel X en muni Y'})
print("Coronel Turismo DIR Listo - Auto NL → Full Army Tourism")

