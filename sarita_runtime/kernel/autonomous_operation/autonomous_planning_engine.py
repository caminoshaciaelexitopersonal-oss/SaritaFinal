import json
import os

class AutonomousPlanningEngine:
    """
    Planning Engine that generates execution sequences, builds dependency graphs,
    and exports required JSON graph descriptors.
    """
    def __init__(self):
        self.current_plan = {}
        self.task_graph = {}
        self.dependency_graph = {}

    def construct_plan(self, approved_decisions: list) -> dict:
        """
        Creates a structured execution plan, resolves dependencies, and optimizes sequence.
        """
        tasks = []
        task_nodes = {}
        dep_nodes = {}

        # 1. Base verification task
        tasks.append({
            "task_id": "TASK-001-SYSTEM-PRECHECK",
            "name": "System Pre-Execution Healthcheck",
            "dependencies": [],
            "risk": 0.05,
            "benefit": 0.95,
            "sequence": 1
        })

        sequence_counter = 2
        for idx, dec in enumerate(approved_decisions):
            task_id = f"TASK-{idx+2:03d}-{dec.node_id}"

            # Sub-divide decision into fine-grained plan tasks
            # Task A: Simulation and safety validation
            task_sim = {
                "task_id": f"{task_id}-SIM",
                "name": f"Simulate execution for {dec.node_id}",
                "dependencies": ["TASK-001-SYSTEM-PRECHECK"],
                "risk": dec.risk * 0.1, # simulation has very low risk
                "benefit": dec.benefit * 0.5,
                "sequence": sequence_counter
            }
            sequence_counter += 1

            # Task B: Real application
            task_app = {
                "task_id": f"{task_id}-APP",
                "name": f"Apply modifications for {dec.node_id}",
                "dependencies": [f"{task_id}-SIM"],
                "risk": dec.risk,
                "benefit": dec.benefit,
                "sequence": sequence_counter
            }
            sequence_counter += 1

            # Task C: Consistency and certification validation
            task_val = {
                "task_id": f"{task_id}-VAL",
                "name": f"Validate and Certify {dec.node_id}",
                "dependencies": [f"{task_id}-APP"],
                "risk": 0.01,
                "benefit": dec.benefit * 0.5,
                "sequence": sequence_counter
            }
            sequence_counter += 1

            tasks.extend([task_sim, task_app, task_val])

        # Optimize task sequence to minimize risk (execute lower risk before higher risk if independent)
        # Note: here we have a linear/tree dependency so sequence numbers are well-ordered.

        self.current_plan = {
            "plan_id": "EP-AUTONOMOUS-PLAN-001",
            "total_tasks": len(tasks),
            "estimated_risk": sum(t["risk"] for t in tasks) / max(1, len(tasks)),
            "estimated_benefit": sum(t["benefit"] for t in tasks) / max(1, len(tasks)),
            "tasks": tasks
        }

        # Build graphs
        self.task_graph = {
            "nodes": [{"id": t["task_id"], "label": t["name"]} for t in tasks],
            "edges": []
        }

        self.dependency_graph = {
            "tasks": {t["task_id"]: t["dependencies"] for t in tasks}
        }

        # Generate edges for task graph and dependency graph representation
        for t in tasks:
            for dep in t["dependencies"]:
                self.task_graph["edges"].append({
                    "from": dep,
                    "to": t["task_id"],
                    "relationship": "must_precede"
                })

        # Save to JSON as required by FASE 131.5
        self._export_graphs()

        return self.current_plan

    def _export_graphs(self):
        """
        Saves execution plan and graphs to disk to meet phase specifications.
        """
        os.makedirs("sarita_runtime/kernel/autonomous_operation", exist_ok=True)

        with open("sarita_runtime/kernel/autonomous_operation/execution_plan.json", "w") as f:
            json.dump(self.current_plan, f, indent=2)

        with open("sarita_runtime/kernel/autonomous_operation/task_graph.json", "w") as f:
            json.dump(self.task_graph, f, indent=2)

        with open("sarita_runtime/kernel/autonomous_operation/dependency_execution_graph.json", "w") as f:
            json.dump(self.dependency_graph, f, indent=2)
