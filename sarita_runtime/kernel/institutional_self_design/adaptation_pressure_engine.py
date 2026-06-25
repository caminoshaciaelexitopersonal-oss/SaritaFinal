import random

class AdaptationPressureEngine:
    def __init__(self):
        pass

    def calculate_pressure(self, civ, ecosystem_metrics):
        # Pressure depends on how far the civ is from the average 'successful' traits
        # or just general environmental volatility
        volatility = random.uniform(0.1, 0.4)
        resource_pressure = 1.0 - (civ.get("resources", 100) / 1000.0)
        return round(max(0.0, min(1.0, volatility + resource_pressure)), 4)
