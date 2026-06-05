# SARITA JavaScript Verifier Specification - Phase 89.4

## Objective
Implement an independent SUEP verifier in Node.js/TypeScript to eliminate language-specific trust dependencies.

## Requirements
1. **No SARITA Source:** Must not use any logic from the original SARITA repo.
2. **Standard Crypto:** Use `crypto` module for SHA-256.
3. **Deterministic JSON:** Use `json-stable-stringify` or equivalent to ensure canonical sorting.

## Algorithm
```javascript
function verifyCausalLink(parentHash, event) {
    const payload = JSON.stringify(event.body, Object.keys(event.body).sort());
    const hash = crypto.createHash('sha256').update(`${parentHash}:${payload}`).digest('hex');
    return hash === event.hash;
}
```

## Compliance
Must match output of `verifier_python.py` for all valid SUEP bundles.
