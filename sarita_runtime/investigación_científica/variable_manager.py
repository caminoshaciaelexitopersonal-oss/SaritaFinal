class VariableManager:
    """
    Manages metadata, roles, scale types, and limits of independent, dependent, and control variables.
    """
    def __init__(self):
        self.variables = {}

    def register_variable(self, name: str, var_type: str, scale_type: str, value_range: tuple = None):
        self.variables[name] = {
            "type": var_type,  # INDEPENDENT, DEPENDENT, CONTROL
            "scale": scale_type,  # CONTINUOUS, CATEGORICAL, ORDINAL, NOMINAL
            "range": value_range
        }

    def get_variables_by_type(self, var_type: str) -> dict:
        return {k: v for k, v in self.variables.items() if v["type"] == var_type}
