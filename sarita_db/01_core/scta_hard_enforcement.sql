-- 30_triggers/scta_hard_enforcement.sql

CREATE OR REPLACE FUNCTION infrastructure.fn_scta_strict_guard()
RETURNS TRIGGER AS $$
BEGIN
    -- Regla 4: Bloqueo absoluto si falta trazabilidad o contexto
    IF NEW.tenant_id IS NULL OR NEW.trace_id IS NULL OR NEW.context_id IS NULL THEN
        RAISE EXCEPTION 'SARITA SCTA SECURITY BREACH: Operación rechazada. Falta (tenant_id, trace_id, context_id) en %.%', TG_TABLE_SCHEMA, TG_TABLE_NAME;
    END IF;

    -- Regla 3: Alimentar ejecución de agente obligatoria
    INSERT INTO ai_core.agent_executions (
        agent_id, context_id, execution_type, input_data, tenant_id, trace_id, execution_status
    ) VALUES (
        (SELECT id FROM ai_core.agents_master WHERE domain_scope @> ARRAY[TG_TABLE_SCHEMA] LIMIT 1),
        NEW.context_id,
        'COGNITIVE_STEP_' || TG_OP,
        row_to_json(NEW)::JSONB,
        NEW.tenant_id,
        NEW.trace_id,
        'COMPLETED'
    );

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Aplicar a dominios críticos (Vía 1, 2, 3 + Finanzas)
-- Nota: En deploy real esto se aplicaría después de las migraciones de ALTER TABLE
