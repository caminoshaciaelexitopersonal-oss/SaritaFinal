class AttentionEconomyManager:
    def distribute_attention(self, institutions):
        total_reputation = sum(i.get("reputation", 1.0) for i in institutions)
        attention_map = {}
        for inst in institutions:
            attention_map[inst["id"]] = inst.get("reputation", 1.0) / total_reputation if total_reputation > 0 else 0
        return attention_map
