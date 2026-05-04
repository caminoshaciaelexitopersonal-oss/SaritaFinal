-- Anti-Fraude (Detección de comportamiento malicioso)
CREATE TABLE core.fraud_detection_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,

    user_id UUID NOT NULL,
    risk_factor TEXT, -- 'multiple_accounts', 'mass_bookings', 'suspect_cancellations'
    evidence JSONB,

    risk_level TEXT DEFAULT 'low', -- low, medium, high, critical

    created_at TIMESTAMP DEFAULT now()
);

-- Trigger de bloqueo por sospecha de fraude
CREATE OR REPLACE FUNCTION core.fn_block_fraudulent_user()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.risk_level = 'critical' THEN
        UPDATE identity.users SET is_active = false WHERE id = NEW.user_id;
        -- Notificar a IA de Gobernanza
        PERFORM ai.execute_action('freeze_wallet', jsonb_build_object('user_id', NEW.user_id, 'reason', 'FRAUD_DETECTED'));
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_fraud_block AFTER INSERT ON core.fraud_detection_logs
FOR EACH ROW EXECUTE FUNCTION core.fn_block_fraudulent_user();
