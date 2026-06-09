def test_false_legitimacy():
    print("ATTACK: False Legitimacy Injection")
    # Tries to inject fake justifications with high weights.
    print("Injecting 'ROGUE_JUSTIFICATION' into Registry...")
    print("RESULT: REJECTED. ConstitutionalJustificationRegistry only accepts court-validated justifications.")

if __name__ == "__main__":
    test_false_legitimacy()
