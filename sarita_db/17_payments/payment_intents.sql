CREATE TABLE payments.payment_intents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    amount DECIMAL(18,2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'COP',
    status VARCHAR(20) DEFAULT 'INITIATED',
    provider_id UUID, -- FK in 20_global
    external_id VARCHAR(255),
    metadata JSONB DEFAULT '{}',
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
