# SARITA Universal Evidence Package (SUEP) Specification V2

## Overview
SUEP is the standard data format for SARITA evidence. It is designed to be language-agnostic and self-describing.

## Structure
```json
{
  "suep_version": "2.0",
  "metadata": {
    "timestamp": "float",
    "producer": "string",
    "schema_hash": "sha256"
  },
  "payload": {
    "initial_state": "object",
    "event_log": "array of events"
  }
}
```

## Canonicalization Rules
1. **JSON Serialization:** All objects must be serialized with keys sorted alphabetically.
2. **Whitespace:** No unnecessary whitespace (compact mode).
3. **Encoding:** UTF-8.
4. **Number Format:** Decimals should avoid scientific notation for maximum cross-language compatibility.

## Verification Logic
A SUEP package is valid if:
1. Every event in `event_log` has a valid causal hash linking to its predecessor.
2. The `initial_state` correctly reflects the system's baseline before the first event.
3. The `schema_hash` matches the expected version.
