-- Guardia de Consistencia Transaccional Cross-Domain
CREATE OR REPLACE FUNCTION core.fn_validate_operation_consistency(p_trace_id UUID)
RETURNS VOID AS $$
DECLARE
    v_events INT;
    v_ledger INT;
    v_payments INT;
BEGIN
    -- Validar que para un trace_id existan registros en los dominios mínimos obligatorios
    SELECT COUNT(*) INTO v_events FROM events.event_store WHERE trace_id = p_trace_id;
    SELECT COUNT(*) INTO v_ledger FROM ledger.transactions WHERE trace_id = p_trace_id;

    -- Los pagos pueden ser opcionales dependiendo de la operación, pero el ledger y event store son mandatorios para trazabilidad.
    IF v_events = 0 OR v_ledger = 0 THEN
        RAISE EXCEPTION 'CRITICAL INCONSISTENCY: Trace % lacks required domain records (Events: %, Ledger: %)', p_trace_id, v_events, v_ledger;
    END IF;
END;
$$ LANGUAGE plpgsql;
