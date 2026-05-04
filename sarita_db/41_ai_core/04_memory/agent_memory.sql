-- 41_ai_core/04_memory/agent_memory.sql
CREATE TABLE ai.agent_memory_global (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    context_id UUID NOT NULL REFERENCES ai.agent_context_universal(id),
    agent_id UUID NOT NULL REFERENCES ai.agents_master(id),
    execution_id UUID, -- Referencia opcional pero recomendada para la trazabilidad de la regla
    memory_scope TEXT NOT NULL, -- LONG_TERM, SHORT_TERM, EPISODIC
    content JSONB NOT NULL,
    relevance_score NUMERIC,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_amg_context ON ai.agent_memory_global(context_id);
CREATE INDEX idx_amg_agent ON ai.agent_memory_global(agent_id);
CREATE INDEX idx_amg_tenant ON ai.agent_memory_global(tenant_id);

-- Regla: No memoria sin ejecución previa
CREATE OR REPLACE FUNCTION ai.fn_trg_memory_execution_check()
RETURNS TRIGGER AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM ai.agent_executions
        WHERE agent_id = NEW.agent_id
        AND context_id = NEW.context_id
    ) THEN
        RAISE EXCEPTION 'SARITA SCTA ERROR: No se puede registrar memoria sin una ejecución previa del agente para el contexto dado';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_memory_execution_check_validation
BEFORE INSERT ON ai.agent_memory_global
FOR EACH ROW EXECUTE FUNCTION ai.fn_trg_memory_execution_check();
