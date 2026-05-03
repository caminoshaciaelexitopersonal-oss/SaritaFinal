CREATE OR REPLACE FUNCTION integrations.verify_webhook_signature(
    payload TEXT,
    signature TEXT,
    p_provider TEXT
)
RETURNS BOOLEAN AS $$
DECLARE
    stored_secret TEXT;
BEGIN
    SELECT secret_hash INTO stored_secret
    FROM integrations.webhook_secrets
    WHERE provider = p_provider
    ORDER BY version DESC LIMIT 1;

    -- Validación usando HMAC SHA256 (Hash determinístico)
    RETURN encode(hmac(payload::bytea, stored_secret::bytea, 'sha256'), 'hex') = signature;
END;
$$ LANGUAGE plpgsql;
