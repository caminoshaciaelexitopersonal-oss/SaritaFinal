CREATE TABLE integrations.webhook_replay_guard (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    signature TEXT UNIQUE NOT NULL,
    received_at TIMESTAMP DEFAULT now()
);

CREATE OR REPLACE FUNCTION integrations.fn_check_webhook_replay(p_signature TEXT)
RETURNS VOID AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM integrations.webhook_replay_guard WHERE signature = p_signature
    ) THEN
        RAISE EXCEPTION 'REPLAY ATTACK DETECTED: Signature % already processed.', p_signature;
    END IF;

    INSERT INTO integrations.webhook_replay_guard (signature) VALUES (p_signature);
END;
$$ LANGUAGE plpgsql;
