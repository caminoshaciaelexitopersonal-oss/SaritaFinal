-- 41_ai_core/07_integration/ai_integration.sql
-- Integración SCTA con dominios críticos de SARITA

-- Función genérica para disparar eventos SCTA
CREATE OR REPLACE FUNCTION ai.fn_scta_trigger_integration()
RETURNS TRIGGER AS $$
DECLARE
    v_context_id UUID;
    v_agent_id UUID;
    v_trace_id UUID;
BEGIN
    -- 1. Intentar capturar trace_id de la sesión o del registro
    v_trace_id := COALESCE(NEW.trace_id, gen_random_uuid()); -- Fallback trace_id si no existe

    -- 2. Buscar o crear contexto para la entidad (Ejemplo simplificado)
    INSERT INTO ai.agent_context_universal (
        tenant_id, domain, entity_type, entity_id, trace_id
    ) VALUES (
        NEW.tenant_id, TG_TABLE_SCHEMA, TG_TABLE_NAME, NEW.id, v_trace_id
    ) ON CONFLICT (id) DO UPDATE SET created_at = now() -- Nota: requiere UNIQUE(entity_type, entity_id) para ser eficiente
    RETURNING id INTO v_context_id;

    -- 3. Identificar Agente Asignado (Mapeado en ai.agent_coverage_matrix)
    SELECT id INTO v_agent_id FROM ai.agents_master
    WHERE specialization = TG_TABLE_NAME OR 'GLOBAL' = ANY(domain_scope)
    LIMIT 1;

    -- 4. Registrar Ejecución Automática (Asíncrona vía Trigger)
    IF v_agent_id IS NOT NULL THEN
        INSERT INTO ai.agent_executions (
            agent_id, context_id, execution_type, input_data, tenant_id, trace_id, execution_status
        ) VALUES (
            v_agent_id, v_context_id, 'SYSTEM_OBSERVATION', row_to_json(NEW)::JSONB, NEW.tenant_id, v_trace_id, 'COMPLETED'
        );
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Aplicar a Pagos
CREATE TRIGGER trg_ai_integration_payments
AFTER INSERT ON payments.payment_intents
FOR EACH ROW EXECUTE FUNCTION ai.fn_scta_trigger_integration();

-- Aplicar a Reservas (Vía 3)
CREATE TRIGGER trg_ai_integration_bookings
AFTER INSERT ON identity.tourist_bookings
FOR EACH ROW EXECUTE FUNCTION ai.fn_scta_trigger_integration();

-- Aplicar a Movimientos Contables
CREATE TRIGGER trg_ai_integration_ledger
AFTER INSERT ON ledger.ledger_entries
FOR EACH ROW EXECUTE FUNCTION ai.fn_scta_trigger_integration();
