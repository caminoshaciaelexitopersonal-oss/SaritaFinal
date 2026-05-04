-- 30_triggers/context_guard.sql

CREATE OR REPLACE FUNCTION ai.fn_trg_context_guard()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.tenant_id IS NULL THEN
        RAISE EXCEPTION 'SARITA SCTA ERROR: tenant_id es obligatorio en el dominio AI';
    END IF;

    IF NEW.trace_id IS NULL THEN
        RAISE EXCEPTION 'SARITA SCTA ERROR: trace_id es obligatorio en el dominio AI';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Aplicar a la tabla de contexto universal
CREATE TRIGGER trg_context_guard_validation
BEFORE INSERT OR UPDATE ON ai.agent_context_universal
FOR EACH ROW EXECUTE FUNCTION ai.fn_trg_context_guard();
