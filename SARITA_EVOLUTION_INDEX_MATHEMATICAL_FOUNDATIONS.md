# Mathematical Foundations of SARITA Evolution Indices
## GMEI, GCEI, and GMCI Formal Definitions

### 1. Global Metaevolution Index (GMEI)
The GMEI quantifies the system's capacity for autonomous redesign and expansion.

**Formula:**
$$GMEI = \sum_{i=1}^{n} w_i \cdot M_i$$

Where:
- $M_1$ (Auto-expansion): Deployed / Requested Capabilities.
- $M_2$ (Adaptability): 1.0 - (Capability Gaps + Architectural Deficits) / Total Required.
- $M_3$ (Safe Evolution): Safety Status binary factor (1.0 if Certified).
- $M_4$ (Sustainable Growth): Mean multi-generational simulation fitness.
- $M_5$ (Future Capability): Justified Designs / Design Target.

**Normalization:**
All submetrics $M_i \in [0, 1]$. Weights $w_i$ sum to 1.0.

---

### 2. Global Constitutional Evolution Index (GCEI)
The GCEI measures the rigor and legality of the evolutionary process.

**Formula:**
$$GCEI = 0.25 \cdot C + 0.20 \cdot S + 0.20 \cdot (1 - R) + 0.15 \cdot T + 0.10 \cdot P + 0.10 \cdot V$$

Variables:
- $C$ (Constitutionality): Mean constitutionality score of approved proposals.
- $S$ (Sovereignty): Identity preservation score $\times$ Core principle invariance.
- $R$ (Risk): Frequency of high/catastrophic risk proposals.
- $T$ (Traceability): Completeness of the causal lineage chain.
- $P$ (Reproducibility): Replay equivalence ratio.
- $V$ (Reversibility): Successful rollback capacity / Total applied changes.

---

### 3. Global Meta-Constitutional Index (GMCI)
The GMCI evaluates the legitimacy and stability of the constitutional layer itself.

**Formula:**
$$GMCI = \frac{0.20 \cdot L + 0.20 \cdot K + 0.15 \cdot E + 0.15 \cdot N + 0.15 \cdot Q + 0.10 \cdot G + 0.05 \cdot H}{1.0}$$

Metrics:
- $L$ (Legitimacy): Normative alignment with Phase 1 foundational intent.
- $K$ (Consistency): Logical consistency index across 1M axioms.
- $E$ (Stability): Multi-generational stability index for foundational principles.
- $N$ (Non-Obsolescence): 1.0 - (Obsolete Axioms / Total Axioms).
- $Q$ (Sovereignty): Meta-sovereignty score over governance layers.
- $G$ (Traceability): Historical lineage depth and validity.
- $H$ (Reproducibility): Constitutional state reconstruction fidelity.

---

### 4. Sensitivity Analysis
- **Axiomatic Shift:** A 1% decay in $K$ (Consistency) triggers a proportional 5% drop in $GMCI$, preventing "stealth" constitutional erosion.
- **Runaway Evolution:** An increase in $M_1$ (Expansion) without a corresponding increase in $M_3$ (Safety) penalizes $GMEI$ exponentially to ensure stability.
- **Sovereignty Breach:** Any $S < 0.9$ in $GCEI$ results in an automatic "PROVISIONAL" status regardless of other scores.
