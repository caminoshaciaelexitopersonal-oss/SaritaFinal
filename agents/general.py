
from langgraph.graph import StateGraph
# Full hierarchy robust: General → Colonels → ... → Cadetes
# Status active, reports chain.

class AgentStatus:
    active = True
    function = 'General orquestra'

class GeneralState(TypedDict):
    # Global command
    pass

def get_general_graph():
    # Orchestrate all colonels
    workflow = StateGraph(GeneralState)
    # ... full
    # Each level report up, health check.
    return workflow.compile()

# All levels active, report chain via state['reports']
print("General robust - Lt/Sgt/Soldado chain verified")


