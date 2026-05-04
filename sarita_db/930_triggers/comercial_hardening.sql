-- Commercial Automation: Event Sourcing & AI
DO $$
DECLARE
    t text;
    s text := 'core';
BEGIN
    FOR t IN
        VALUES ('leads_erp', 'sales_order_items', 'social_messages', 'ai_chat_sessions', 'ai_sales_actions', 'omnichannel_conversion', 'marketing_campaigns')
    LOOP
        -- Trigger para Event Sourcing
        EXECUTE format('DROP TRIGGER IF EXISTS trg_es_%I ON %I.%I;', t, s, t);
        EXECUTE format('CREATE TRIGGER trg_es_%I AFTER INSERT OR UPDATE ON %I.%I FOR EACH ROW EXECUTE FUNCTION events.fn_capture_event();', t, s, t);

        -- Trigger para Notificación IA
        EXECUTE format('DROP TRIGGER IF EXISTS trg_ai_%I ON %I.%I;', t, s, t);
        EXECUTE format('CREATE TRIGGER trg_ai_%I AFTER INSERT OR UPDATE ON %I.%I FOR EACH ROW EXECUTE FUNCTION ai_memory.fn_notify_ai_agent();', t, s, t);
    END LOOP;
END;
$$;
