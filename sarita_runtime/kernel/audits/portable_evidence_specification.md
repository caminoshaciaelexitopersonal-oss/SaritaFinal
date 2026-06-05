# Portable Evidence Specification (Phase 87.5)

## 1. Evidence Package Structure (JSON)
The Sovereign Evidence Package is a self-contained, cryptographically signed bundle of all data required for independent verification.

```json
{
  "version": "1.0",
  "package_hash": "SHA-256",
  "data": {
    "state": {
      "ownership": { "resource_id": "owner_id" },
      "pressure": 0.0
    },
    "events": [
      {
        "vertex_id": "UUID",
        "parent_hash": "SHA-256",
        "hash": "SHA-256",
        "payload": {}
      }
    ]
  }
}
```

## 2. Verification Protocol
1. **Uniqueness:** Verify `package_hash`.
2. **Lineage:** Verify the `parent_hash` chain of all events.
3. **Replay:** Reconstruct `state` using `ExternalReplayEngine` and compare hashes.

## 3. Conclusion
The specification allows any standard-compliant auditor to verify SARITA legitimacy without access to the kernel's binary or source code.
