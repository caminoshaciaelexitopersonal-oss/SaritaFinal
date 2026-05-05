-- Triggers de Monitoreo Transaccional para IA
CREATE OR REPLACE FUNCTION ai_core.fn_monitor_fraud_and_abandonment()
RETURNS TRIGGER AS $$
BEGIN
    -- Si es sesión WPC y lleva más de 30 mins sin convertir
    IF TG_TABLE_NAME = 'wpc_sessions' AND NEW.status = 'abandonado' THEN
        INSERT INTO ai_core.agent_events (source_table, record_id, event_payload, tenant_id)
        VALUES ('core.wpc_sessions', NEW.id, jsonb_build_object('reason', 'abandonment'), NEW.tenant_id);

    -- Si el intento de pago falla repetidamente
    ELSIF TG_TABLE_NAME = 'payment_attempts' AND NEW.status = 'FAILED' THEN
        INSERT INTO ai_core.agent_events (source_table, record_id, event_payload, tenant_id)
        VALUES ('finance.payment_attempts', NEW.id, jsonb_build_object('warning', 'potential_fraud'), NEW.tenant_id);
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_ai_fraud ON finance.payment_attempts;
CREATE TRIGGER trg_ai_fraud AFTER INSERT ON finance.payment_attempts FOR EACH ROW EXECUTE FUNCTION ai_core.fn_monitor_fraud_and_abandonment();
