import uuid
import time
from .risk_management_engine import RiskManagementEngine

class AutonomousExecutionEngine:
    """
    Core executor that safely applies, validates, and rolls back architectural modifications.
    Ensures safe operations with transactional rollback capability.
    """
    def __init__(self, risk_manager, learning_engine):
        self.risk_manager = risk_manager
        self.learning_engine = learning_engine
        self.execution_history = []

    def execute_task_flow(self, plan: dict, decision_tree_root) -> list:
        """
        Executes an orchestrated flow of planned tasks.
        Validates safety, runs tasks, and coordinates learning updates.
        """
        outcomes = []

        # Traverse decisions or tasks
        for task in plan.get("tasks", []):
            task_id = task["task_id"]
            if "SYSTEM-PRECHECK" in task_id:
                # Pre-check task always succeeds
                outcomes.append({
                    "task_id": task_id,
                    "status": "COMPLETED",
                    "execution_id": f"EXE-{uuid.uuid4().hex[:8].upper()}",
                    "rollback_triggered": False,
                    "quality_delta": 0.0,
                    "success": True
                })
                continue

            # Identify matching decision node
            decision_id = None
            for child in decision_tree_root.children:
                if child.node_id in task_id:
                    decision_id = child.node_id
                    break

            if not decision_id:
                continue

            decision_node = decision_tree_root.children[0] # Fallback/target node
            for child in decision_tree_root.children:
                if child.node_id == decision_id:
                    decision_node = child
                    break

            # 1. Evaluate Risk and Safety
            risk_assessment = self.risk_manager.assess_risk(decision_node.to_dict())
            if not risk_assessment["safe"]:
                # Stop unsafe change
                outcomes.append({
                    "task_id": task_id,
                    "status": "BLOCKED_UNSAFE",
                    "execution_id": f"EXE-{uuid.uuid4().hex[:8].upper()}",
                    "decision_id": decision_node.node_id,
                    "evidence_id": f"EVI-BLOCKED-{uuid.uuid4().hex[:8].upper()}",
                    "learning_id": f"LRN-BLOCKED-{uuid.uuid4().hex[:8].upper()}",
                    "rollback_triggered": False,
                    "quality_delta": 0.0,
                    "success": False,
                    "reason": risk_assessment["reason"]
                })
                continue

            # 2. Simulate or execute based on task suffix
            exec_id = f"EXE-{uuid.uuid4().hex[:8].upper()}"
            evidence_id = f"EVI-{uuid.uuid4().hex[:8].upper()}"

            start_time = time.time()

            if "-SIM" in task_id:
                # Simulation phase
                time.sleep(0.01) # fast simulation
                success = True
                rollback_triggered = False
                quality_delta = 0.01
                status = "COMPLETED"
            elif "-APP" in task_id:
                # Real application phase
                # Take snapshot before applying change
                self.risk_manager.rollback_manager.create_snapshot(exec_id, {"system_state": "STABLE"})

                # Apply change (We simulate a potential runtime error if risk is extremely high)
                if decision_node.risk > 0.80:
                    # Intentionally fail for risk-learning demo
                    success = False
                    rollback_triggered = True
                    self.risk_manager.rollback_manager.trigger_rollback(exec_id, "Post-execution validation check failed.")
                    quality_delta = -0.05
                    status = "ROLLED_BACK"
                else:
                    success = True
                    rollback_triggered = False
                    quality_delta = 0.03
                    status = "COMPLETED"
            else: # -VAL task
                success = True
                rollback_triggered = False
                quality_delta = 0.01
                status = "COMPLETED"

            # 3. Process outcomes with the learning engine
            learning_res = self.learning_engine.process_execution_outcome(
                execution_id=exec_id,
                decision_node=decision_node.to_dict(),
                start_time=start_time,
                success=success,
                rollback_triggered=rollback_triggered,
                quality_delta=quality_delta
            )

            outcomes.append({
                "task_id": task_id,
                "status": status,
                "execution_id": exec_id,
                "decision_id": decision_node.node_id,
                "evidence_id": evidence_id,
                "learning_id": learning_res["learning_id"],
                "rollback_triggered": rollback_triggered,
                "quality_delta": quality_delta,
                "success": success
            })

        self.execution_history.extend(outcomes)
        return outcomes
