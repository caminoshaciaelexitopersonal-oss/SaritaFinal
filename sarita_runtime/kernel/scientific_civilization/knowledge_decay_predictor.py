class KnowledgeDecayPredictor:
    def predict_decay(self, access_frequency, update_rate):
        # Knowledge decays if not accessed or updated
        return 1.0 / (access_frequency * update_rate) if access_frequency > 0 else 1.0
