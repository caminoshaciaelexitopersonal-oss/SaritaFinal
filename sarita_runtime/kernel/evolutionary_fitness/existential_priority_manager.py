class ExistentialPriorityManager:
    """
    Manages priorities when existential risks are detected.
    """
    def set_existential_priority(self, p_e: float):
        if p_e > 0.1:
            return "EXTREMELY_HIGH"
        return "NORMAL"
