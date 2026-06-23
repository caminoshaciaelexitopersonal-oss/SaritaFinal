class InstitutionSurvivalValidator:
    def validate_survival(self, inst):
        # Checks if institution still meets core civilizational criteria
        return inst.get("active") is True and inst.get("age", 0) > 0
