-- 10.12_tourist_v3/ai_behavioral_triggers.sql
-- Triggers para alimentar la IA con comportamiento del turista
CREATE OR REPLACE FUNCTION identity.fn_trg_tourist_behavior_to_ai()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO ai_core.agent_events (
        agent_id,
        event_type,
        payload,
        tenant_id,
        trace_id
    ) VALUES (
        'TOURIST_AI_ENGINE',
        TG_TABLE_NAME || '_' || TG_OP,
        row_to_json(NEW)::JSONB,
        NEW.tenant_id,
        NEW.trace_id
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Aplicar a búsquedas
CREATE TRIGGER trg_tourist_search_to_ai
AFTER INSERT ON identity.tourist_searches
FOR EACH ROW EXECUTE FUNCTION identity.fn_trg_tourist_behavior_to_ai();

-- Aplicar a reservas
CREATE TRIGGER trg_tourist_booking_to_ai
AFTER INSERT OR UPDATE ON identity.tourist_bookings
FOR EACH ROW EXECUTE FUNCTION identity.fn_trg_tourist_behavior_to_ai();
