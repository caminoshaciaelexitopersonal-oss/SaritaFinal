import logging
import os

class RuntimeThermalAuthority:
    """
    Governs thermal pressure physically.
    """
    def __init__(self):
        self.thermal_base = "/sys/class/thermal"

    async def get_highest_zone_temperature(self):
        max_temp = 0.0
        try:
            for zone in os.listdir(self.thermal_base):
                if zone.startswith("thermal_zone"):
                    temp_path = os.path.join(self.thermal_base, zone, "temp")
                    if os.path.exists(temp_path):
                        with open(temp_path, "r") as f:
                            temp = int(f.read().strip()) / 1000.0
                            if temp > max_temp:
                                max_temp = temp
            return max_temp
        except Exception as e:
            logging.error(f"Thermal Authority: Error reading temperature: {e}")
            return 0.0

    async def audit_thermal_compliance(self, threshold_c: float = 85.0):
        temp = await self.get_highest_zone_temperature()
        logging.info(f"Thermal Authority: Max zone temperature: {temp}C")
        return temp < threshold_c
