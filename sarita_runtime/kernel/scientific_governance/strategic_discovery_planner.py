class StrategicDiscoveryPlanner:
    def plan_discovery(self, priorities):
        # Plans the next set of discoveries based on high-priority domains
        top_priorities = sorted(priorities.items(), key=lambda x: x[1], reverse=True)[:3]
        return [{"domain": p[0], "goal": "MAXIMIZE_KNOWLEDGE"} for p in top_priorities]
