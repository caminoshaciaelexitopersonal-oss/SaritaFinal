-- Reconstrucción de estado desde Event Store
CREATE OR REPLACE FUNCTION events.fn_rebuild_state(p_aggregate_id UUID)
RETURNS JSONB AS $$
DECLARE
    v_state JSONB := '{}';
    v_event RECORD;
BEGIN
    FOR v_event IN
        SELECT payload
        FROM events.event_store
        WHERE aggregate_id = p_aggregate_id
        ORDER BY version ASC
    LOOP
        v_state := v_state || v_event.payload;
    END LOOP;

    RETURN v_state;
END;
$$ LANGUAGE plpgsql;
