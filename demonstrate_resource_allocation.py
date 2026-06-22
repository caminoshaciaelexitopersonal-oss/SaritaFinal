from sarita_runtime.kernel.scientific_governance.research_resource_engine import ResearchResourceEngine

def run_demo():
    engine = ResearchResourceEngine()
    domains = [
        {"id": "D1", "priority": 0.9},
        {"id": "D2", "priority": 0.5},
        {"id": "D3", "priority": 0.2}
    ]

    print("Managing research resource allocation...")
    mgmt = engine.manage_resources(domains, global_uncertainty=0.7)

    print("Cognitive Budget Allocations:", mgmt["allocations"])
    print("Exploration/Exploitation Balance:", mgmt["balance"])

if __name__ == "__main__":
    run_demo()
