-- Estrategia de Archiving de Eventos
CREATE TABLE events.event_store_archive (LIKE events.event_store INCLUDING ALL);

CREATE OR REPLACE FUNCTION events.fn_archive_old_events(p_months INT DEFAULT 12)
RETURNS INT AS $$
DECLARE
    v_count INT;
BEGIN
    WITH moved_rows AS (
        DELETE FROM events.event_store
        WHERE created_at < now() - (p_months || ' months')::interval
        RETURNING *
    )
    INSERT INTO events.event_store_archive SELECT * FROM moved_rows;

    GET DIAGNOSTICS v_count = ROW_COUNT;
    RETURN v_count;
END;
$$ LANGUAGE plpgsql;
