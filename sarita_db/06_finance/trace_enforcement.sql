CREATE OR REPLACE FUNCTION core.enforce_trace_id()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.trace_id IS NULL THEN
        RAISE EXCEPTION 'Traceability Error: trace_id is required in %', TG_TABLE_NAME;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Aplicación a tablas críticas
DROP TRIGGER IF EXISTS trg_trace_enforcement ON finance.transactions;
CREATE TRIGGER trg_trace_enforcement BEFORE INSERT ON finance.transactions FOR EACH ROW EXECUTE FUNCTION core.enforce_trace_id();

DROP TRIGGER IF EXISTS trg_trace_enforcement ON finance.payment_intents;
CREATE TRIGGER trg_trace_enforcement BEFORE INSERT ON finance.payment_intents FOR EACH ROW EXECUTE FUNCTION core.enforce_trace_id();

DROP TRIGGER IF EXISTS trg_trace_enforcement ON events.event_store;
CREATE TRIGGER trg_trace_enforcement BEFORE INSERT ON events.event_store FOR EACH ROW EXECUTE FUNCTION core.enforce_trace_id();

DROP TRIGGER IF EXISTS trg_trace_enforcement ON auditoria.system_logs;
CREATE TRIGGER trg_trace_enforcement BEFORE INSERT ON auditoria.system_logs FOR EACH ROW EXECUTE FUNCTION core.enforce_trace_id();
