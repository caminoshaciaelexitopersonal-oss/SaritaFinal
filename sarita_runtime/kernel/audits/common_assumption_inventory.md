# Common Assumption Inventory - Phase 90.1

1. **SHA-256 Integrity:** All verifiers assume SHA-256 is collision-resistant for the lifetime of the evidence.
2. **Deterministic Time:** All verifiers assume NTP or hardware clocks are sufficiently synchronized for timestamp validation.
3. **Canonical JSON:** All verifiers assume that alphabetical key sorting is enough for determinism.
4. **Ownership Persistence:** Verifiers assume that once an ownership is registered in the graph, its lineage is unbreakable.
5. **Protocol Versioning:** Verifiers assume that "version 2.0" means the same thing across all implementations.

## Mitigation Strategy (Phase 90)
- Implement `ImplementationDiversityEngine` to penalize shared language/author.
- Implement `MetaConsensusEngine` to detect if consensuses are derived from the same implementation family.
