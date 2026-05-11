# SARITA LIVE ORCHESTRATION (Temporal.io)

## 1. WORKFLOW: FINANCIAL SAGA
**Objective:** Atomic cross-domain transactions (Booking + Payment + Commission).

### Activities:
1. `ReserveHotelSlot`: Locks inventory in Tourism domain.
2. `AuthorizePayment`: Validates balance in Finance domain.
3. `CalculateCommission`: Triggers Marketplace worker logic.
4. `SettleLedger`: Final atomic entry in accounting.

### Compensation Strategy:
- If `AuthorizePayment` fails -> `ReleaseHotelSlot`.
- If `SettleLedger` fails -> `RefundAuthorization` + `NotifyTenant`.

## 2. WORKFLOW: CRISIS RECOVERY
**Objective:** Automated system healing during incidents.

### Activities:
1. `IdentifyCorruptionSource`: Scans memory and trace hashes.
2. `IsolationQuarantine`: Blocks affected tenant/agent.
3. `RollbackSovereignState`: Reverts to last known good snapshot.
4. `RebuildIntegrityHashes`: Recalculates `hash_integridad` for consistency.
