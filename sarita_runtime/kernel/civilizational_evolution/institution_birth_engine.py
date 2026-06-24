import uuid
import random

class InstitutionBirthEngine:
    def trigger_birth(self, ecosystem_state):
        new_id = str(uuid.uuid4())
        institution = {
            "id": new_id,
            "type": random.choice(["RESEARCH", "GOVERNANCE", "ECONOMY", "CULTURE"]),
            "fitness": 0.5,
            "resources": 1.0,
            "age": 0,
            "alliances": [],
            "status": "BIRTH"
        }
        return institution
