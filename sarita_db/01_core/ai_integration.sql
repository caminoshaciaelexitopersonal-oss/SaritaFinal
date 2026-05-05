-- Triggers de Integración IA (Fase Lanzamiento)

-- Sincronizar eventos críticos de comportamiento hacia el bus de agentes
DO $$
DECLARE
    t text;
BEGIN
    FOR t IN VALUES ('tourist_searches', 'fraud_detection_logs', 'wpc_intents')
    LOOP
        EXECUTE format('DROP TRIGGER IF EXISTS trg_ai_%I ON core.%I;', t, t);
        EXECUTE format('CREATE TRIGGER trg_ai_%I AFTER INSERT OR UPDATE ON core.%I FOR EACH ROW EXECUTE FUNCTION ai_memory.fn_notify_ai_agent();', t, t);
    END LOOP;
END;
$$;
