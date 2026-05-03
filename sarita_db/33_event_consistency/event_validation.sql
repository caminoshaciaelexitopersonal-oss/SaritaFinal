CREATE OR REPLACE FUNCTION events.validate_event_sequence()
RETURNS TRIGGER AS $$
DECLARE
    last_version INT;
BEGIN
    SELECT MAX(version)
    INTO last_version
    FROM events.event_store
    WHERE aggregate_id = NEW.aggregate_id;

    -- Si no es el primer evento, la versión debe ser exactamente la anterior + 1
    IF last_version IS NOT NULL AND NEW.version != last_version + 1 THEN
        RAISE EXCEPTION 'Invalid event sequence for aggregate %: Expected %, got %', NEW.aggregate_id, last_version + 1, NEW.version;
    ELSIF last_version IS NULL AND NEW.version != 1 THEN
        RAISE EXCEPTION 'Invalid event sequence: First event for aggregate % must be version 1, got %', NEW.aggregate_id, NEW.version;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_validate_event_sequence ON events.event_store;
CREATE TRIGGER trg_validate_event_sequence
BEFORE INSERT ON events.event_store
FOR EACH ROW
EXECUTE FUNCTION events.validate_event_sequence();
