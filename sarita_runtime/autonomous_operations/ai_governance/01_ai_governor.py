class AIGovernor:
    def __init__(self):
        self.forbidden_tools = ["drop_database", "delete_all_tenants"]
        self.privileged_tools = ["freeze_tenant", "authorize_unusual_payment"]

    def validate_action(self, agent_id, tool_name, auth_level):
        print(f"Auditing AI Action: {agent_id} -> {tool_name}")

        if tool_name in self.forbidden_tools:
            return False, "FORBIDDEN_OPERATION"

        if tool_name in self.privileged_tools and auth_level < 5:
            return False, "INSUFFICIENT_PRIVILEGES"

        return True, "AUTHORIZED"

    def apply_throttling(self, agent_id, current_pressure):
        if current_pressure > 0.9:
            print(f"THROTTLING agent {agent_id}: Cognitive pressure too high.")
            return True
        return False

if __name__ == "__main__":
    gov = AIGovernor()
    allowed, reason = gov.validate_action("Tactical-01", "freeze_tenant", 3)
    print(f"Status: {allowed}, Reason: {reason}")
