-- Detección de Abandono (Crítico para WPC y Conversión)
CREATE OR REPLACE FUNCTION core.fn_check_checkout_abandonment()
RETURNS TRIGGER AS $$
BEGIN
    -- Si la sesión pasa a estado 'inactivo' o 'abandonado' (manejado por app o scheduler)
    IF NEW.session_status = 'abandonada' AND OLD.session_status = 'activa' THEN
        INSERT INTO core.tourist_events (user_id, event_type, payload, tenant_id, trace_id)
        VALUES (NEW.user_id, 'abandon', jsonb_build_object('session_id', NEW.id, 'step', 'checkout'), NEW.tenant_id, NEW.trace_id);

        -- Notificar a IA
        PERFORM ai_memory.fn_notify_ai_agent();
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_abandon_check AFTER UPDATE ON core.tourist_sessions
FOR EACH ROW EXECUTE FUNCTION core.fn_check_checkout_abandonment();
