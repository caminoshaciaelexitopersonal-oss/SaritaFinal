-- Motor Transaccional Unificado
CREATE OR REPLACE FUNCTION core.fn_execute_financial_operation(p_tenant_id UUID, p_payload JSONB) RETURNS UUID AS $$
DECLARE v_trace_id UUID; v_context_id UUID; v_trans_id UUID;
BEGIN
    v_trace_id := (p_payload->>'trace_id')::UUID;
    v_context_id := (p_payload->>'context_id')::UUID;
    INSERT INTO events.event_store (aggregate_id, aggregate_type, event_type, payload, tenant_id, trace_id, context_id)
    VALUES (COALESCE((p_payload->>'aggregate_id')::UUID, gen_random_uuid()), p_payload->>'aggregate_type', p_payload->>'event_type', p_payload, p_tenant_id, v_trace_id, v_context_id);
    INSERT INTO ledger.transactions (tenant_id, trace_id, context_id, reference)
    VALUES (p_tenant_id, v_trace_id, v_context_id, 'FIN-' || v_trace_id) RETURNING id INTO v_trans_id;
    RETURN v_trans_id;
END; $$ LANGUAGE plpgsql;
