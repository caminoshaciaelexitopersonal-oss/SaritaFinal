-- Operational Automation: Event Sourcing & AI
DO $$
DECLARE
    t text;
    s text;
BEGIN
    -- Tablas críticas en core
    FOR t IN VALUES ('service_orders_erp', 'bookings_erp', 'operational_tasks')
    LOOP
        EXECUTE format('DROP TRIGGER IF EXISTS trg_es_%I ON core.%I;', t, t);
        EXECUTE format('CREATE TRIGGER trg_es_%I AFTER INSERT OR UPDATE ON core.%I FOR EACH ROW EXECUTE FUNCTION events.fn_capture_event();', t, t);

        EXECUTE format('DROP TRIGGER IF EXISTS trg_ai_%I ON core.%I;', t, t);
        EXECUTE format('CREATE TRIGGER trg_ai_%I AFTER INSERT OR UPDATE ON core.%I FOR EACH ROW EXECUTE FUNCTION ai_core.fn_notify_ai_agent();', t, t);
    END LOOP;

    -- Tablas críticas en tourism (especializada)
    FOR t IN VALUES ('kitchen_orders', 'transport_trips')
    LOOP
        EXECUTE format('DROP TRIGGER IF EXISTS trg_es_%I ON tourism.%I;', t, t);
        EXECUTE format('CREATE TRIGGER trg_es_%I AFTER INSERT OR UPDATE ON tourism.%I FOR EACH ROW EXECUTE FUNCTION events.fn_capture_event();', t, t);

        EXECUTE format('DROP TRIGGER IF EXISTS trg_ai_%I ON tourism.%I;', t, t);
        EXECUTE format('CREATE TRIGGER trg_ai_%I AFTER INSERT OR UPDATE ON tourism.%I FOR EACH ROW EXECUTE FUNCTION ai_core.fn_notify_ai_agent();', t, t);
    END LOOP;
END;
$$;
