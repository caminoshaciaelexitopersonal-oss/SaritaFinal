import uuid
from .civilizational_simulation_engine import Civilization

class CivilizationBuilder:
    """
    Instantiates a new civilization from a MetaConstitution.
    """
    def build(self, meta_constitution):
        civ_id = f"CIV-{uuid.uuid4().hex[:8].upper()}"
        return Civilization(civ_id, meta_constitution)
