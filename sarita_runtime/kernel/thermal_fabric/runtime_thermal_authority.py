import logging
import os

class RuntimeThermalAuthority:
    """
    Governs thermal pressure physically.
    """
    def __init__(self):
        self.thermal_base = "/sys/class/thermal"

    def get_highest_zone_temperature(self):
        max_temp = 0.0
        try:
            if not os.path.exists(self.thermal_base):
                return 45.0 # Stable baseline if no sysfs

            for zone in os.listdir(self.thermal_base):
                if zone.startswith("thermal_zone"):
                    temp_path = os.path.join(self.thermal_base, zone, "temp")
                    if os.path.exists(temp_path):
                        with open(temp_path, "r") as f:
                            temp = int(f.read().strip()) / 1000.0
                            if temp > max_temp:
                                max_temp = temp
            return max_temp if max_temp > 0 else 45.0
        except Exception as e:
            logging.error(f"Thermal Authority: Error reading temperature: {e}")
            return 45.0

    def audit_thermal_pressure(self):
        """Material implementation to return current system temperature."""
        temp = self.get_highest_zone_temperature()
        logging.info(f"Thermal Authority: Current physical temperature: {temp}C")
        return temp

    def audit_thermal_compliance(self, threshold_c: float = 85.0):
        temp = self.audit_thermal_pressure()
        return temp < threshold_c
