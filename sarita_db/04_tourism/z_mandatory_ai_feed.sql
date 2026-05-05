-- 30_triggers/z_mandatory_ai_feed.sql
-- Integración Total AI Core (Misión 5)

CREATE OR REPLACE FUNCTION infrastructure.fn_feed_scta()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO ai_core.agent_executions (
        agent_id, context_id, execution_type, input_data, tenant_id, trace_id, execution_status
    ) VALUES (
        (SELECT id FROM ai_core.agents_master WHERE domain_scope @> ARRAY[TG_TABLE_SCHEMA] LIMIT 1),
        NEW.context_id,
        'AUTO_FEED_' || TG_OP,
        row_to_json(NEW)::JSONB,
        NEW.tenant_id,
        NEW.trace_id,
        'COMPLETED'
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers para cada vía
DO $$
DECLARE
    t text;
BEGIN
    -- Vía 1
    CREATE TRIGGER trg_ai_v1 AFTER INSERT ON governance.administrative_acts FOR EACH ROW EXECUTE FUNCTION infrastructure.fn_feed_scta();
    -- Vía 2
    CREATE TRIGGER trg_ai_v2 AFTER INSERT ON erp.business_operations FOR EACH ROW EXECUTE FUNCTION infrastructure.fn_feed_scta();
    -- Vía 3
    CREATE TRIGGER trg_ai_v3 AFTER INSERT ON tourism.booking_reservations FOR EACH ROW EXECUTE FUNCTION infrastructure.fn_feed_scta();
EXCEPTION WHEN OTHERS THEN
    NULL; -- Evitar que falle el deploy si las tablas no existen aún en el orden de carga
END $$;
