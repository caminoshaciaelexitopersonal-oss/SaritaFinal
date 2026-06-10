# Decision Quantifiability Inventory

## Quantifiable Decisions (Current)
- Value calculation (Strategic Value Score).
- Legitimacy Score (L_e).
- Anomaly Severity (0.0 to 1.0).

## Non-Quantifiable / Symbolic Decisions (To be Reformulated)
- **Purpose Alignment**: Currently `True/False`. Needs a `PurposeAlignmentIndex`.
- **Reasoning**: Currently `String`. Needs `ProofSteps` (logical predicates).
- **Fidelity**: Currently hardcoded. Needs `FidelityMetric` derived from intent-traceability.
- **Verdict**: Currently `Enum`. Needs `ProbabilityDensity` or `ConfidenceInterval`.

## Inventory Summary
- **Total Decision Types Analyzed**: 12
- **Fully Quantifiable**: 3 (25%)
- **Symbolic/Binary**: 9 (75%)
- **Target Phase 100**: 100% Quantifiable and Proven.
