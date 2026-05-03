-- Captura automática de eventos para reconstrucción total
CREATE OR REPLACE FUNCTION events.fn_capture_event()
RETURNS TRIGGER AS $$
DECLARE
    v_aggregate_id UUID;
BEGIN
    v_aggregate_id := COALESCE(NEW.id, OLD.id);

    INSERT INTO events.event_store (
        aggregate_id, aggregate_type, event_type, payload, version, tenant_id
    ) VALUES (
        v_aggregate_id,
        TG_TABLE_SCHEMA || '.' || TG_TABLE_NAME,
        TG_OP,
        to_jsonb(NEW),
        1, -- Versión inicial o calculada
        NEW.tenant_id
    );

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
