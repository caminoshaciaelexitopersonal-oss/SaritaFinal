CREATE TABLE core.webhook_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    provider_name VARCHAR(100),
    external_id VARCHAR(255),
    event_type VARCHAR(100),
    payload JSONB NOT NULL,
    processed BOOLEAN DEFAULT false,
    trace_id UUID,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

CREATE TABLE core.webhook_signatures (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    provider_name VARCHAR(100) UNIQUE,
    secret_key TEXT NOT NULL,
    algorithm VARCHAR(50) DEFAULT 'sha256',
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

CREATE OR REPLACE FUNCTION core.fn_verify_webhook_signature(
    p_provider TEXT,
    p_payload TEXT,
    p_signature TEXT
) RETURNS BOOLEAN AS $$
DECLARE
    v_secret TEXT;
BEGIN
    SELECT secret_key INTO v_secret FROM core.webhook_signatures WHERE provider_name = p_provider;
    RETURN p_signature = encode(hmac(p_payload::bytea, v_secret::bytea, 'sha256'), 'hex');
END;
$$ LANGUAGE plpgsql;
