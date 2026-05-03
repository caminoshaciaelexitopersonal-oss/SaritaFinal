-- Integración de sistema real con ecosistema IA (Agentes)
CREATE TABLE ai_memory.agent_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_table VARCHAR(100) NOT NULL,
    record_id UUID NOT NULL,
    event_payload JSONB NOT NULL,
    ai_status VARCHAR(20) DEFAULT 'UNPROCESSED', -- UNPROCESSED, ANALYZED, ACTION_TAKEN
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

-- Función notificadora
CREATE OR REPLACE FUNCTION ai_memory.fn_notify_ai_agent()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO ai_memory.agent_events (source_table, record_id, event_payload, tenant_id)
    VALUES (TG_TABLE_SCHEMA || '.' || TG_TABLE_NAME, COALESCE(NEW.id, OLD.id), to_jsonb(NEW), NEW.tenant_id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Activación en tablas críticas para que la IA "vea" la realidad
DROP TRIGGER IF EXISTS trg_ai_notify_payments ON payments.payment_intents;
CREATE TRIGGER trg_ai_notify_payments AFTER INSERT OR UPDATE ON payments.payment_intents FOR EACH ROW EXECUTE FUNCTION ai_memory.fn_notify_ai_agent();

DROP TRIGGER IF EXISTS trg_ai_notify_ledger ON ledger.ledger_entries;
CREATE TRIGGER trg_ai_notify_ledger AFTER INSERT ON ledger.ledger_entries FOR EACH ROW EXECUTE FUNCTION ai_memory.fn_notify_ai_agent();

-- Incidencias (Suponiendo tabla existiese en governance o operativo)
-- CREATE TRIGGER trg_ai_notify_incidents AFTER INSERT ON erp_operativo.incidents FOR EACH ROW EXECUTE FUNCTION ai_memory.fn_notify_ai_agent();
