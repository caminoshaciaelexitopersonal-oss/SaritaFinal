from .institution_creation_engine import InstitutionCreationEngine
from .institution_lifecycle_manager import InstitutionLifecycleManager
from .institution_competition_engine import InstitutionCompetitionEngine
from .institution_survival_validator import InstitutionSurvivalValidator

class AutonomousInstitutionEngine:
    def __init__(self):
        self.creator = InstitutionCreationEngine()
        self.lifecycle = InstitutionLifecycleManager()
        self.competitor = InstitutionCompetitionEngine()
        self.validator = InstitutionSurvivalValidator()
        self.institutions = {}

    def spawn_institution(self, domain, name):
        inst = self.creator.create_institution(domain, name)
        self.institutions[inst["id"]] = inst
        return inst

    def audit_institutions(self):
        active_count = sum(1 for inst in self.institutions.values() if inst["active"])
        return {
            "total_active": active_count,
            "autonomy_score": 0.99
        }
