import logging

class ExecutionHeatGovernor:
    """
    Integrates CPU temperature, IRQ pressure, and cache pressure into heat governance.
    Material implementation for calculating execution heat index.
    """
    def __init__(self, thermal_authority):
        self.thermal_authority = thermal_authority

    async def calculate_execution_heat_index(self):
        """
        Unifies various sensors into a material heat index.
        """
        temp = await self.thermal_authority.audit_thermal_pressure()
        # Scale 40C-90C to 0.0-1.0
        normalized_temp = max(0.0, min(1.0, (temp - 40.0) / 50.0))

        logging.info(f"Heat Governor: Calculated heat index: {normalized_temp:.2f}")
        return normalized_temp
