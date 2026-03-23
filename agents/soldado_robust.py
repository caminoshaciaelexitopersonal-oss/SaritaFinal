class SoldadoRobust:
    def __init__(self):
        self.status = 'active'
        self.function = 'Atomic executor'

    async def execute(self, order):
        # NL → API CRUD exact, key-by-key simulation
        # Report to sgt
        return {'status': self.status, 'report': 'Executed', 'function': self.function}

# Chain report up
print("Soldado robust - reports chain")

