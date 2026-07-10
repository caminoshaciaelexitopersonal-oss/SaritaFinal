class CertificationDashboard:
    def render(self, state_manager) -> dict:
        return {
            "title": "Global Certification",
            "validation_score": state_manager.certification.validation_score,
            "certified_phases": state_manager.certification.certified_phases
        }
