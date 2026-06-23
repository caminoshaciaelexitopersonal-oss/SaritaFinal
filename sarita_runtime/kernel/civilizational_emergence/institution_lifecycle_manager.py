class InstitutionLifecycleManager:
    def update_lifecycle(self, institution, resources):
        # Institutions age and can disappear if resources are exhausted
        institution["age"] += 1
        if resources < 0.1:
            institution["active"] = False
            return "DISSOLVED"
        return "ACTIVE"
