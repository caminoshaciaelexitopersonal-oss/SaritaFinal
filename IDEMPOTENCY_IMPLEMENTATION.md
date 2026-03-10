# IDEMPOTENCY IMPLEMENTATION: SARITA v1.0
**Status:** IMPLEMENTED
**Lead Architect:** Jules

## 1. Idempotency Standard
The system implements the `Idempotency-Key` header standard for all critical POST, PUT, and DELETE operations.
- **Model**: `IdempotencyKey` in `sarita_agents` app.
- **Scope**: Per-domain isolation (Wallet, Ledger, AI Misiones).

## 2. Validation Logic
When a request with an `Idempotency-Key` is received:
1. **Check**: Verify if the key exists for the specific domain in the `IdempotencyKey` table.
2. **Handle**:
   - If status is `SUCCESS`, return the cached `response_payload`.
   - If status is `PENDING`, return a `409 Conflict` indicating the operation is already in progress.
   - If not found, proceed with the execution and mark as `PENDING`.
3. **Commit**: Upon successful completion, update the status to `SUCCESS` and store the result.

## 3. Critical Path Integration
- **N6 Soldado Oro V2**: Automatically handles idempotency at the atomic micro-task level.
- **Ledger Engine**: Uses the `financial_event_id` or `reference` as a natural idempotency key to prevent duplicate accounting impacts.
- **Wallet Service**: Integrated into `execute_complex_transaction` to prevent double-spending during retries.

## 4. Key Retention
- **Table**: `sarita_agents_idempotencykey`
- **Fields**: `key`, `domain`, `status`, `response_payload`, `created_at`.
- **Cleanup**: Keys are retained for 7 days by default (Configurable).

---
**Verdict**: Idempotency is fully operational, preventing duplicate transactions and ensuring consistent retries.
