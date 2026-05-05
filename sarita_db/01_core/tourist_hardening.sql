-- Triggers de Comportamiento del Turista
CREATE OR REPLACE FUNCTION tourism.fn_trg_capture_tourist_event()
RETURNS TRIGGER AS $$
BEGIN
    -- Capturar automáticamente el evento de creación/modificación como comportamiento
    INSERT INTO core.tourist_events (user_id, event_type, payload, tenant_id, trace_id)
    VALUES (NEW.user_id, TG_TABLE_NAME || '_' || TG_OP, to_jsonb(NEW), NEW.tenant_id, NEW.trace_id);

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Aplicar a favoritos y reseñas
CREATE TRIGGER trg_capture_fav AFTER INSERT ON core.tourist_favorites FOR EACH ROW EXECUTE FUNCTION tourism.fn_trg_capture_tourist_event();
CREATE TRIGGER trg_capture_rev AFTER INSERT ON core.tourist_reviews_extended FOR EACH ROW EXECUTE FUNCTION tourism.fn_trg_capture_tourist_event();
