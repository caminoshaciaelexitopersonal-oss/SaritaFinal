CREATE TABLE payments.payment_attempts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    payment_intent_id UUID NOT NULL, -- FK in 20_global
    attempt_number INTEGER NOT NULL,
    status VARCHAR(20) NOT NULL,
    error_code VARCHAR(100),
    error_message TEXT,
    payload JSONB DEFAULT '{}',
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
