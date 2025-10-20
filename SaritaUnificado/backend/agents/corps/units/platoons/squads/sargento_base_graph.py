from typing import TypedDict, Any, List, Annotated
import operator
# from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import StateGraph, END, START
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
# Potencialmente para otros proveedores:
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.tools import BaseTool
from api.models import CustomUser


class SargentoBaseState(TypedDict):
    """La pizarra táctica estandarizada para todos los Sargentos."""
    teniente_order: str
    app_context: dict  # Se espera que contenga {'user': CustomUser}
    messages: Annotated[List[BaseMessage], operator.add]
    final_report: str
    error: str | None


class SargentoGraphBuilder:
    """
    Constructor estandarizado para agentes Sargento.
    Construye un grafo que utiliza el proveedor de IA y la clave de API
    específicos del usuario que realiza la solicitud.
    """

    def __init__(self, squad: List[BaseTool], squad_name: str):
        self.squad = squad
        self.squad_name = squad_name
        self.squad_executor = ToolNode(self.squad)

    def get_sargento_brain(self, state: SargentoBaseState):
        """
        El cerebro del Sargento. Construye dinámicamente el LLM con las
        credenciales del usuario y decide la siguiente acción.
        """
        print(f"--- 🤔 SARGENTO ({self.squad_name}): Analizando orden para el usuario... ---")

        user = state['app_context'].get('user')
        if not isinstance(user, CustomUser) or not user.api_key or not user.ai_provider:
            raise ValueError("Contexto de aplicación inválido o configuración de IA del usuario incompleta.")

        # --- Lógica Multi-Inquilino ---
        # Se instancia el modelo de lenguaje específico basado en la configuración del usuario.
        api_key = user.api_key

        if user.ai_provider == CustomUser.AIProvider.OPENAI:
            model = ChatOpenAI(model="gpt-4o", temperature=0, api_key=api_key)
        # elif user.ai_provider == CustomUser.AIProvider.GOOGLE:
        #     model = ChatGoogleGenerativeAI(
        #         model="gemini-pro",
        #         google_api_key=api_key,
        #         convert_system_message_to_human=True
        #     )
        else:
            raise NotImplementedError(f"Proveedor de IA '{user.ai_provider}' no soportado.")

        # Se enlazan las herramientas de la escuadra al modelo específico del usuario.
        bound_model = model.bind_tools(self.squad)

        return bound_model.invoke(state["messages"])

    def route_action(self, state: SargentoBaseState):
        """Revisa la decisión del cerebro y enruta al ejecutor o al informe final."""
        last_message = state["messages"][-1]
        if not hasattr(last_message, 'tool_calls') or not last_message.tool_calls:
            return "compile_report"
        return "squad_executor"

    def compile_report_node(self, state: SargentoBaseState) -> SargentoBaseState:
        """Compila el informe final para el Teniente a partir del historial de la misión."""
        print(f"--- 📄 SARGENTO ({self.squad_name}): Misión completada. Compilando reporte. ---")
        final_ai_message = state["messages"][-1].content
        executed_steps = [
            f"Acción: {msg.name}, Resultado: {msg.content}"
            for msg in state["messages"] if msg.type == 'tool'
        ]

        if not executed_steps:
            report_body = "Misión completada sin necesidad de acciones directas de la escuadra."
        else:
            report_body = "Resumen de acciones de la escuadra:\n- " + "\n- ".join(executed_steps)

        state["final_report"] = f"{final_ai_message}\n\n---\n**Bitácora de Ejecución:**\n{report_body}"
        return state

    def build_graph(self):
        """Construye y compila el grafo LangGraph para el Sargento."""
        workflow = StateGraph(SargentoBaseState)

        def mission_entry_node(state: SargentoBaseState):
            """Nodo de entrada que formatea la orden del Teniente como el primer mensaje."""
            return {"messages": [HumanMessage(content=state["teniente_order"])]}

        workflow.add_node("mission_entry", mission_entry_node)
        workflow.add_node("brain", self.get_sargento_brain)
        workflow.add_node("squad_executor", self.squad_executor)
        workflow.add_node("compile_report", self.compile_report_node)

        workflow.add_edge(START, "mission_entry")
        workflow.add_edge("mission_entry", "brain")
        workflow.add_conditional_edges("brain", self.route_action, {
            "squad_executor": "squad_executor",
            "compile_report": "compile_report"
        })
        workflow.add_edge("squad_executor", "brain")
        workflow.add_edge("compile_report", END)

        return workflow.compile()