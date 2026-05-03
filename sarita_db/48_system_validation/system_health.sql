-- Validación Global de Salud de Datos
CREATE OR REPLACE FUNCTION core.fn_check_system_health()
RETURNS JSONB AS $$
DECLARE
    v_ledger_balance DECIMAL;
    v_orphans INT;
    v_result JSONB;
BEGIN
    -- 1. Balance Ledger Global
    SELECT SUM(debit - credit) INTO v_ledger_balance FROM ledger.ledger_entries;

    -- 2. Transacciones sin Eventos (Huérfanas)
    SELECT COUNT(*) INTO v_orphans
    FROM ledger.transactions t
    LEFT JOIN events.event_store e ON t.id = e.event_id
    WHERE e.event_id IS NULL;

    v_result := jsonb_build_object(
        'ledger_integrity', CASE WHEN v_ledger_balance = 0 THEN 'OK' ELSE 'FAIL' END,
        'ledger_diff', v_ledger_balance,
        'orphan_transactions', v_orphans,
        'status', CASE WHEN v_ledger_balance = 0 AND v_orphans = 0 THEN 'HEALTHY' ELSE 'CRITICAL' END,
        'checked_at', now()
    );

    RETURN v_result;
END;
$$ LANGUAGE plpgsql;
