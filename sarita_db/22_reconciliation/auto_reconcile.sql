-- Motor de Conciliación Automática Profesional
CREATE OR REPLACE FUNCTION reconciliation.fn_auto_reconcile(p_tenant_id UUID)
RETURNS TABLE(match_exact INTEGER, match_tolerable INTEGER, inconsistencies INTEGER) AS $$
DECLARE
    v_exact INTEGER := 0;
    v_tolerable INTEGER := 0;
    v_inconsistent INTEGER := 0;
BEGIN
    -- 1. Match Exacto (Monto + Referencia)
    INSERT INTO reconciliation.matches (movement_id, ledger_transaction_id, match_type, confidence_score, tenant_id)
    SELECT
        m.id, t.id, 'EXACT', 1.0, p_tenant_id
    FROM reconciliation.bank_movements m
    JOIN ledger.transactions t ON m.reference = t.reference
    JOIN ledger.ledger_entries e ON e.transaction_id = t.id
    WHERE m.tenant_id = p_tenant_id AND m.match_status = 'UNMATCHED'
    AND ABS(m.amount) = ABS(e.debit - e.credit)
    ON CONFLICT DO NOTHING;
    GET DIAGNOSTICS v_exact = ROW_COUNT;

    -- 2. Diferencia Tolerable (Monto con margen < 1%)
    INSERT INTO reconciliation.matches (movement_id, ledger_transaction_id, match_type, confidence_score, tenant_id)
    SELECT
        m.id, t.id, 'TOLERABLE', 0.8, p_tenant_id
    FROM reconciliation.bank_movements m
    JOIN ledger.transactions t ON m.reference = t.reference
    JOIN ledger.ledger_entries e ON e.transaction_id = t.id
    WHERE m.tenant_id = p_tenant_id AND m.match_status = 'UNMATCHED'
    AND ABS(ABS(m.amount) - ABS(e.debit - e.credit)) / NULLIF(ABS(m.amount), 0) < 0.01
    ON CONFLICT DO NOTHING;
    GET DIAGNOSTICS v_tolerable = ROW_COUNT;

    -- Actualizar estados de movimientos
    UPDATE reconciliation.bank_movements SET match_status = 'MATCHED'
    WHERE id IN (SELECT movement_id FROM reconciliation.matches WHERE tenant_id = p_tenant_id);

    -- Identificar Inconsistencias (Referencia igual, monto muy diferente)
    SELECT COUNT(*) INTO v_inconsistent
    FROM reconciliation.bank_movements m
    JOIN ledger.transactions t ON m.reference = t.reference
    WHERE m.tenant_id = p_tenant_id AND m.match_status = 'UNMATCHED';

    RETURN QUERY SELECT v_exact, v_tolerable, v_inconsistent;
END;
$$ LANGUAGE plpgsql;
