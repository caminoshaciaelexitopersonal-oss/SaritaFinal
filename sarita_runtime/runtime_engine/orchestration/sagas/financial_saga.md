# SAGA FINANCIERA DISTRIBUIDA
**Workflow:** `FinancialSagaWorkflow`

## 1. PASOS DE EJECUCIÓN (ACTIVITIES)
1. **ReserveInventory:** (Tourism Domain) - Bloquea el cupo del hotel/tour.
2. **AuthorisePayment:** (Finance Domain) - Valida saldo y reserva fondos.
3. **ConfirmBooking:** (Tourism Domain) - Cambia estado a 'Confirmado'.
4. **SettlePayment:** (Finance Domain) - Ejecuta el movimiento real de dinero.

## 2. ESTRATEGIA DE COMPENSACIÓN (ROLLBACK)
- Si `AuthorisePayment` falla -> `ReleaseInventory` (Compensación de paso 1).
- Si `SettlePayment` falla -> `CancelBooking` + `RefundAuthorisation`.

## 3. TIMEOUTS
- `ReserveInventory`: 10 seconds.
- `AuthorisePayment`: 30 seconds.
- Saga Completa: 2 minutes.
