-- Trigger: Validar respaldo en ledger para salidas de efectivo
CREATE OR REPLACE FUNCTION core.fn_validate_cash_outflow_ledger()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.movement_type = 'egreso' THEN
        -- Validar que exista un asiento contable vinculado (vía trace_id o external_reference)
        IF NOT EXISTS (SELECT 1 FROM accounting.journal_entries WHERE trace_id = NEW.trace_id) THEN
            RAISE EXCEPTION 'Falla de Integridad Financiera: El egreso de caja debe tener un respaldo contable (Asiento)';
        END IF;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_validate_cash_ledger ON core.cash_movements;
CREATE TRIGGER trg_validate_cash_ledger AFTER INSERT ON core.cash_movements
FOR EACH ROW EXECUTE FUNCTION core.fn_validate_cash_outflow_ledger();
