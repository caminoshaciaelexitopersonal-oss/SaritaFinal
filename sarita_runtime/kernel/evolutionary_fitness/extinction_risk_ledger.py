import time

class ExtinctionRiskLedger:
    """
    Stores historical records of extinction risk analysis.
    """
    def __init__(self):
        self.risks = []

    def record_risk(self, p_e: float, risk_level: str):
        self.risks.append({"p_e": p_e, "level": risk_level, "time": time.time()})
        print(f"EXTINCTION RISK LEDGER: Recorded P_e: {p_e}")
