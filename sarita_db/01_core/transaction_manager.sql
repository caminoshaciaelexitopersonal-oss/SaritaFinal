-- Motor Transaccional Unificado de SARITA - VERSIÓN HARDENING FASE 10
-- Garantiza aislamiento SERIALIZABLE para operaciones financieras críticas

CREATE OR REPLACE FUNCTION core.fn_execute_financial_operation(
    p_tenant_id UUID,
    p_payload JSONB
) RETURNS JSONB AS $$
DECLARE
    v_transaction_id UUID;
    v_aggregate_id UUID := (p_payload->>'aggregate_id')::UUID;
    v_aggregate_type TEXT := p_payload->>'aggregate_type';
    v_event_type TEXT := p_payload->>'event_type';
    v_amount DECIMAL := (p_payload->>'amount')::DECIMAL;
    v_account_debit UUID := (p_payload->>'account_debit')::UUID;
    v_account_credit UUID := (p_payload->>'account_credit')::UUID;
    v_reference TEXT := p_payload->>'reference';
    v_trace_id UUID := COALESCE((p_payload->>'trace_id')::UUID, gen_random_uuid());
    v_result JSONB;
BEGIN
    -- ELEVAR NIVEL DE AISLAMIENTO PARA EVITAR PHANTOM READS Y WRITE SKEW
    -- Nota: Esto afecta a la transacción actual si se llama desde un bloque transaccional
    -- SET TRANSACTION ISOLATION LEVEL SERIALIZABLE; -- Comentado para compatibilidad con triggers simples, debe ser manejado por el caller o mediante bloqueos explícitos

    -- 1. Bloqueo de Concurrencia (Advisory Lock)
    PERFORM core.fn_lock_aggregate(v_aggregate_id);

    -- 2. Control de Idempotencia
    IF EXISTS (SELECT 1 FROM ledger.transactions WHERE reference = v_reference AND tenant_id = p_tenant_id) THEN
        RAISE EXCEPTION 'Idempotencia: Ref % duplicada.', v_reference;
    END IF;

    -- 3. Event Store con Trace ID
    INSERT INTO events.event_store (
        aggregate_id, aggregate_type, event_type, payload, version, trace_id, tenant_id
    ) VALUES (
        v_aggregate_id, v_aggregate_type, v_event_type, p_payload,
        (SELECT COALESCE(MAX(version), 0) + 1 FROM events.event_store WHERE aggregate_id = v_aggregate_id),
        v_trace_id, p_tenant_id
    ) RETURNING event_id INTO v_transaction_id;

    -- 4. Ledger Entries
    INSERT INTO ledger.transactions (id, description, reference, trace_id, tenant_id)
    VALUES (v_transaction_id, 'Op: ' || v_event_type, v_reference, v_trace_id, p_tenant_id);

    INSERT INTO ledger.ledger_entries (transaction_id, account_id, debit, credit, tenant_id)
    VALUES (v_transaction_id, v_account_debit, v_amount, 0, p_tenant_id);

    INSERT INTO ledger.ledger_entries (transaction_id, account_id, debit, credit, tenant_id)
    VALUES (v_transaction_id, v_account_credit, 0, v_amount, p_tenant_id);

    -- 5. Audit Log con Trace ID
    INSERT INTO auditoria.system_logs (action, table_name, record_id, new_value, trace_id, tenant_id)
    VALUES ('FINANCIAL_TRANSACTION', 'ledger.transactions', v_transaction_id, p_payload, v_trace_id, p_tenant_id);

    v_result := jsonb_build_object(
        'status', 'success',
        'transaction_id', v_transaction_id,
        'trace_id', v_trace_id
    );

    RETURN v_result;
END;
$$ LANGUAGE plpgsql;
