class RuntimeMirror:
    def __init__(self):
        self.virtual_state = {}

    def sync_state(self, real_state):
        self.virtual_state = real_state
        print("Digital Twin Synchronized with Real Runtime.")

    def simulate_scenario(self, scenario):
        print(f"Simulating Scenario on Twin: {scenario}")
        # Lógica de proyección de impacto
        impact_score = 0.85
        return impact_score

if __name__ == "__main__":
    twin = RuntimeMirror()
    twin.sync_state({"finance": "HEALTHY", "ai_load": 0.4})
    score = twin.simulate_scenario("KAFKA_BROKER_DEATH")
    print(f"Estimated Impact Score: {score}")
