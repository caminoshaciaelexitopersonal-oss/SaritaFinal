class SelfImprovementEngine:
    """
    Self-Improvement loop coordinator.
    Reads metrics, detects opportunities, generates proposals,
    prioritizes them, runs them, and repeats to achieve global optimality.
    """
    def __init__(self, operation_engine):
        self.op_engine = operation_engine

    def execute_closed_loop_improvement(self, rounds: int = 2) -> list:
        """
        Executes multiple sequential rounds of self-improvement.
        Returns the history of improvements and index evolution.
        """
        loop_history = []

        for r in range(rounds):
            # 1. Analyze state and scan for inefficiencies
            proposals = self.op_engine.optimization_engine.scan_for_inefficiencies()

            # 2. Filter and prioritize based on current policies
            prioritized = self.op_engine.optimization_engine.consolidate_inefficiencies(proposals)

            # 3. Decision-making tree construction
            decision_tree_root = self.op_engine.decision_engine.construct_decision_tree(prioritized)

            # 4. Filter only approved/low risk nodes for current round
            approved_nodes = [node for node in decision_tree_root.children if node.score >= 0.2]

            # 5. Planning
            plan = self.op_engine.planning_engine.construct_plan(approved_nodes)

            # 6. Safety Audit and Execution
            outcomes = self.op_engine.execution_engine.execute_task_flow(plan, decision_tree_root)

            # 7. Evaluate GAOI improvements
            gaoi_res = self.op_engine.calculate_gaoi_index()

            loop_history.append({
                "round": r + 1,
                "proposals_found": len(proposals),
                "executed_tasks": len(outcomes),
                "final_gaoi": gaoi_res["gaoi"],
                "outcomes": outcomes
            })

        return loop_history
