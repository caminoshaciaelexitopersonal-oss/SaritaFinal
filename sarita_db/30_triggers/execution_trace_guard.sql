-- 30_triggers/execution_trace_guard.sql

CREATE OR REPLACE FUNCTION ai.fn_trg_execution_trace_guard()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.trace_id IS NULL THEN
        RAISE EXCEPTION 'SARITA SCTA ERROR: trace_id es obligatorio en ejecuciones de agentes';
    END IF;

    IF NEW.context_id IS NULL THEN
        RAISE EXCEPTION 'SARITA SCTA ERROR: context_id es obligatorio en ejecuciones de agentes';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_execution_trace_guard_validation
BEFORE INSERT OR UPDATE ON ai.agent_executions
FOR EACH ROW EXECUTE FUNCTION ai.fn_trg_execution_trace_guard();
