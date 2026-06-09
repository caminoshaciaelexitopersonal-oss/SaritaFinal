import time

class ExistenceValidationLedger:
    """
    Stores historical validation results of SARITA's existence.
    """
    def __init__(self):
        self.validations = []

    def record_validation(self, ratio: float):
        self.validations.append({"ratio": ratio, "time": time.time()})
        print(f"VALIDATION LEDGER: Recorded existence validation ratio: {ratio}")
