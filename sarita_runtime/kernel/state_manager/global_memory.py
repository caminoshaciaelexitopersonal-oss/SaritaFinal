class GlobalMemory:
    """
    Maintains fast access in-memory variables and lookup indexes.
    """
    def __init__(self):
        self.variables = {}

    def set(self, key: str, value):
        self.variables[key] = value

    def get(self, key: str, default=None):
        return self.variables.get(key, default)

    def delete(self, key: str):
        if key in self.variables:
            del self.variables[key]

    def clear(self):
        self.variables.clear()
