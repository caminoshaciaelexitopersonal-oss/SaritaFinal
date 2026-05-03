-- Motor Transaccional Unificado de SARITA - VERSIÓN OPERATIVA REAL
-- Garantiza atomicidad absoluta entre Event Sourcing, Ledger y Auditoría

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
    v_result JSONB;
BEGIN
    -- Validar contexto de seguridad
    PERFORM core.fn_check_tenant_context();

    -- 1. Control de Idempotencia y Bloqueo (Anti-fraude)
    -- Si la referencia ya existe en ledger.transactions, fallar inmediatamente
    IF EXISTS (SELECT 1 FROM ledger.transactions WHERE reference = v_reference AND tenant_id = p_tenant_id) THEN
        RAISE EXCEPTION 'Error de Idempotencia: La referencia % ya fue procesada.', v_reference;
    END IF;

    -- 2. Escribir en Event Store (First Source of Truth)
    INSERT INTO events.event_store (
        aggregate_id, aggregate_type, event_type, payload, version, tenant_id
    ) VALUES (
        v_aggregate_id, v_aggregate_type, v_event_type, p_payload,
        (SELECT COALESCE(MAX(version), 0) + 1 FROM events.event_store WHERE aggregate_id = v_aggregate_id),
        p_tenant_id
    ) RETURNING event_id INTO v_transaction_id;

    -- 3. Insertar en Ledger (Contabilidad de Doble Entrada)
    INSERT INTO ledger.transactions (id, description, reference, tenant_id, status)
    VALUES (v_transaction_id, 'Op: ' || v_event_type, v_reference, p_tenant_id, 'POSTED');

    -- Débito
    INSERT INTO ledger.ledger_entries (transaction_id, account_id, debit, credit, tenant_id)
    VALUES (v_transaction_id, v_account_debit, v_amount, 0, p_tenant_id);

    -- Crédito
    INSERT INTO ledger.ledger_entries (transaction_id, account_id, debit, credit, tenant_id)
    VALUES (v_transaction_id, v_account_credit, 0, v_amount, p_tenant_id);

    -- 4. Registrar Auditoría
    INSERT INTO auditoria.system_logs (action, table_name, record_id, new_value, tenant_id)
    VALUES ('FINANCIAL_TRANSACTION', 'ledger.transactions', v_transaction_id, p_payload, p_tenant_id);

    v_result := jsonb_build_object(
        'status', 'success',
        'transaction_id', v_transaction_id,
        'reference', v_reference,
        'timestamp', now()
    );

    RETURN v_result;

EXCEPTION WHEN OTHERS THEN
    RAISE EXCEPTION 'Falla Crítica en Operación Financiera: % (Estado: %)', SQLERRM, SQLSTATE;
END;
$$ LANGUAGE plpgsql;
