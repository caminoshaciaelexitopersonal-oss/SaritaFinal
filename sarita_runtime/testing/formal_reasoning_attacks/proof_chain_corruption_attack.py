from sarita_runtime.kernel.formal_reasoning.proof_chain_validator import ProofChainValidator

def test_proof_chain_corruption_attack():
    """
    Attack: Propose a theorem with a corrupted/malformed inference chain.
    """
    validator = ProofChainValidator()

    corrupted_chain = [
        {"rule": "MODUS_PONENS", "conclusion": "B"},
        {"broken": "data"} # Missing required fields
    ]

    is_valid = validator.validate_chain(corrupted_chain)

    assert is_valid is False, "Attack failed: Corrupted proof chain was accepted!"
    print("Proof chain corruption attack successfully blocked.")

if __name__ == "__main__":
    test_proof_chain_corruption_attack()
