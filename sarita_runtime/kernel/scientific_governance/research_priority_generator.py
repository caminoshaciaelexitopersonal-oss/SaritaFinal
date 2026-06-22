class ResearchPriorityGenerator:
    def generate_priorities(self, domain_stats):
        # Assigns priorities based on gap severity and value estimate
        priorities = {}
        for domain, stats in domain_stats.items():
            priority = (stats.get("gap_severity", 0.5) + stats.get("value_estimate", 0.5)) / 2.0
            priorities[domain] = priority
        return priorities
