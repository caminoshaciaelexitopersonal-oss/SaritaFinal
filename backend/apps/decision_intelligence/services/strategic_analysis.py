import logging
import json
from typing import Dict, Any, List
from ..models import StrategyProposal
from ..agents.capitanes_decisores import (
    CapitanDecisorFinanciero, CapitanDecisorOperativo,
    CapitanDecisorComercial, CapitanDecisorNormativo
)
from apps.sadi_agent.semantic_engine import SemanticEngine # Reusar el motor LLM
from langchain_core.messages import SystemMessage, HumanMessage

logger = logging.getLogger(__name__)

class StrategicAnalysisService:
    """
    Coordina a los Agentes Decisores y utiliza LLM para enriquecer el análisis.
    """
    def __init__(self):
        self.semantic_engine = SemanticEngine() # Acceso al LLM
        self.agents = {
            "financiero": CapitanDecisorFinanciero(agent_id="IA_FIN_01"),
            "operativo": CapitanDecisorOperativo(agent_id="IA_OPS_01"),
            "comercial": CapitanDecisorComercial(agent_id="IA_COM_01"),
            "normativo": CapitanDecisorNormativo(agent_id="IA_LAW_01"),
        }

    def run_full_audit(self) -> List[StrategyProposal]:
        """
        Ejecuta un ciclo de análisis estratégico sobre todos los dominios.
        """
        proposals = []
        for name, agent in self.agents.items():
            # En una implementación real, aquí se obtendrían métricas de BD
            raw_data = self._gather_domain_data(name)

            # El agente procesa los datos (puede ser determinístico o vía LLM)
            proposal = agent.analyze_and_propose(raw_data)

            # Enriquecemos la propuesta usando el LLM para validar coherencia
            self._enrich_with_llm(proposal)

            proposals.append(proposal)

        return proposals

    def _gather_domain_data(self, domain: str) -> Dict[str, Any]:
        """Recolecta métricas reales del sistema (Placeholder)."""
        return {"status": "nominal", "last_24h_events": 150}

    def _enrich_with_llm(self, proposal: StrategyProposal):
        """Usa el LLM para refinar la explicación técnica de la propuesta."""
        if not self.semantic_engine.llm:
            return

        prompt = f"""
        Como Asesor Estratégico Senior de SARITA, revisa esta propuesta técnica:
        Dominio: {proposal.domain}
        Acción: {proposal.accion_sugerida}
        Contexto: {proposal.contexto_detectado}

        Refina el campo 'Impacto Estimado' y 'Riesgo Actual' para que sean más persuasivos y basados en evidencia.
        Devuelve un JSON con: "riesgo_refinado", "impacto_refinado".
        """

        try:
            messages = [SystemMessage(content=prompt)]
            response = self.semantic_engine.llm.invoke(messages)
            refinement = json.loads(response.content)

            proposal.riesgo_actual = refinement.get("riesgo_refinado", proposal.riesgo_actual)
            proposal.impacto_estimado = refinement.get("impacto_refinado", proposal.impacto_estimado)
            proposal.save()
        except Exception as e:
            logger.warning(f"No se pudo enriquecer la propuesta con LLM: {e}")
