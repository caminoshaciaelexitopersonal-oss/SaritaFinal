import logging

class RuntimeReclaimPredictor:
    """
    Predicts memory pressure and triggers reclaim before host VM.
    """
    def __init__(self, nervous_system):
        self.nervous_system = nervous_system

    def predict_reclaim_urgency(self, current_usage_bytes: int, limit_bytes: int):
        ratio = current_usage_bytes / limit_bytes
        logging.info(f"Reclaim Predictor: Memory usage ratio {ratio:.2f}")
        return ratio > 0.85
