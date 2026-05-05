-- Artisan Automation: Event Sourcing & AI
DO $$
DECLARE
    t text;
    s text := 'tourism';
BEGIN
    FOR t IN
        VALUES ('artisans', 'artisan_products', 'artisan_inventory', 'artisan_production_orders', 'artisan_ratings')
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

-- Sincronización Automática con Directorio
CREATE OR REPLACE FUNCTION tourism.fn_sync_artisan_directory()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO tourism.artisan_directory_index (artisan_id, nombre_busqueda, tenant_id, trace_id)
    VALUES (NEW.id, NEW.especialidad, NEW.tenant_id, NEW.trace_id)
    ON CONFLICT (artisan_id) DO UPDATE SET last_sync = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_sync_directory AFTER INSERT ON tourism.artisans FOR EACH ROW EXECUTE FUNCTION tourism.fn_sync_artisan_directory();
