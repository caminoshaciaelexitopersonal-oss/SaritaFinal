-- Test de Integridad Financiera (Ledger)
DO $$
DECLARE
    v_diff DECIMAL;
BEGIN
    SELECT SUM(debit - credit) INTO v_diff FROM ledger.ledger_entries;
    IF v_diff != 0 THEN
        RAISE EXCEPTION 'Falla de Integridad: El ledger global no cuadra (%)', v_diff;
    END IF;
    RAISE NOTICE 'Test Ledger: PASSED';
END;
$$;

-- Test de RLS (Verificación de aislamiento)
-- [Requiere simular sesión de tenant]
