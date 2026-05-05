-- Bloqueos Críticos de Vía 2 (Hardening de Negocio)

-- 1. Impedir transacciones si la licencia no está activa
CREATE OR REPLACE FUNCTION tourism.fn_check_provider_license()
RETURNS TRIGGER AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM tourism.provider_licenses
        WHERE provider_id = NEW.provider_id
        AND estado = 'activo'
        AND (fecha_expiracion IS NULL OR fecha_expiracion > CURRENT_DATE)
    ) THEN
        RAISE EXCEPTION 'Operación Bloqueada: El prestador % no tiene una licencia activa o vigente.', NEW.provider_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 2. Impedir transacciones si la reputación es crítica (< 2.0)
CREATE OR REPLACE FUNCTION tourism.fn_check_provider_reputation()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM tourism.provider_reputation_score
        WHERE provider_id = NEW.provider_id
        AND score_global < 2.0
    ) THEN
        RAISE EXCEPTION 'Operación Bloqueada: El prestador % tiene una reputación crítica.', NEW.provider_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Aplicar a eventos y capacidad
DROP TRIGGER IF EXISTS trg_check_license_event ON tourism.provider_events;
CREATE TRIGGER trg_check_license_event BEFORE INSERT ON tourism.provider_events FOR EACH ROW EXECUTE FUNCTION tourism.fn_check_provider_license();

DROP TRIGGER IF EXISTS trg_check_reputation_event ON tourism.provider_events;
CREATE TRIGGER trg_check_reputation_event BEFORE INSERT ON tourism.provider_events FOR EACH ROW EXECUTE FUNCTION tourism.fn_check_provider_reputation();

-- Auditoría y Event Sourcing (incluyendo el bloque anterior)
DO $$
DECLARE
    t text;
    s text := 'tourism';
BEGIN
    FOR t IN
        VALUES ('tourism_providers', 'provider_roles', 'provider_events', 'provider_reviews', 'provider_capacity', 'provider_licenses', 'provider_structure')
    LOOP
        -- Trigger para Event Sourcing
        EXECUTE format('DROP TRIGGER IF EXISTS trg_es_%I ON %I.%I;', t, s, t);
        EXECUTE format('CREATE TRIGGER trg_es_%I AFTER INSERT OR UPDATE ON %I.%I FOR EACH ROW EXECUTE FUNCTION events.fn_capture_event();', t, s, t);

        -- Trigger para Notificación IA
        EXECUTE format('DROP TRIGGER IF EXISTS trg_ai_%I ON %I.%I;', t, s, t);
        EXECUTE format('CREATE TRIGGER trg_ai_%I AFTER INSERT OR UPDATE ON %I.%I FOR EACH ROW EXECUTE FUNCTION ai_core.fn_notify_ai_agent();', t, s, t);
    END LOOP;
END;
$$;
