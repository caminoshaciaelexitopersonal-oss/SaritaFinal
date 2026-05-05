-- Test de desacoplamiento de triggers
-- Intento con trace_id cero (debe permitir sin context_id)
INSERT INTO finance.payment_intents (tenant_id, trace_id, context_id, amount)
VALUES ('00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000000', NULL, 100);

-- Intento normal sin context_id (debe fallar en payment_intents)
-- INSERT INTO finance.payment_intents (tenant_id, trace_id, context_id, amount)
-- VALUES ('00000000-0000-0000-0000-000000000001', gen_random_uuid(), NULL, 100);
