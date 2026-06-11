import uuid
import random
from .meta_constitution_engine import MetaConstitution

class ConstitutionalArchetypeGenerator:
    """
    Generates specific MetaConstitution archetypes based on design coordinates.
    """

    ARCHETYPES = [
        "SovereignMonolith",
        "AdaptiveSwarm",
        "RigidImmutable",
        "RecursiveEvolver",
        "StoicFortress",
        "ExpansionistLogic"
    ]

    def generate(self, coordinates):
        meta_id = f"META-{uuid.uuid4().hex[:8].upper()}"
        archetype_name = self._determine_archetype(coordinates)

        meta = MetaConstitution(meta_id, origin=f"ArchetypeGenerator:{archetype_name}")

        # Populate with traits based on coordinates
        meta.axioms = [f"AXIOM-{archetype_name.upper()}-{i}" for i in range(3)]

        meta.governance_structure = {
            "type": "Centralized" if coordinates.get("centralization", 0.5) > 0.5 else "Decentralized",
            "authority_concentration": coordinates.get("centralization", 0.5),
            "hierarchy_depth": int(coordinates.get("complexity", 0.5) * 10)
        }

        meta.evolution_rules = {
            "mutation_rate": coordinates.get("volatility", 0.1),
            "crossover_probability": 1.0 - coordinates.get("centralization", 0.5),
            "drift_tolerance": 1.0 - coordinates.get("rigidity", 0.5)
        }

        meta.selection_rules = {
            "primary_metric": "Stability" if coordinates.get("rigidity", 0.5) > 0.5 else "Adaptability",
            "selection_pressure": coordinates.get("complexity", 0.5)
        }

        meta.adaptation_rules = {
            "learning_rate": coordinates.get("volatility", 0.5),
            "feedback_sensitivity": coordinates.get("complexity", 0.5)
        }

        meta.survival_rules = {
            "min_ps_threshold": 0.3 + (coordinates.get("rigidity", 0.5) * 0.4),
            "recovery_multiplier": 1.0 + coordinates.get("volatility", 0.5)
        }

        meta.termination_rules = {
            "extinction_threshold": 0.1,
            "max_drift_allowed": 0.4
        }

        return meta

    def _determine_archetype(self, coords):
        # Simplified logic to map coordinates to archetype names
        if coords.get("centralization", 0) > 0.8: return "SovereignMonolith"
        if coords.get("volatility", 0) > 0.8: return "AdaptiveSwarm"
        if coords.get("rigidity", 0) > 0.8: return "RigidImmutable"
        if coords.get("complexity", 0) > 0.8: return "RecursiveEvolver"

        return random.choice(self.ARCHETYPES)
