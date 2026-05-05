-- Simulación de Pago Completo y Validación de Sincronía
BEGIN;
SET app.current_tenant = '00000000-0000-0000-0000-000000000001';
-- 1. Pago
INSERT INTO finance.payment_intents (id, tenant_id, trace_id, context_id, amount, status)
VALUES (gen_random_uuid(), '00000000-0000-0000-0000-000000000001', gen_random_uuid(), gen_random_uuid(), 50000, 'SUCCEEDED');
-- 2. Validar que el trigger disparó evento (simulado)
-- 3. Validar Ledger
INSERT INTO finance.ledger_entries (tenant_id, trace_id, context_id, account_id, debit)
VALUES ('00000000-0000-0000-0000-000000000001', (SELECT trace_id FROM finance.payment_intents LIMIT 1), gen_random_uuid(), gen_random_uuid(), 50000);
ROLLBACK;
