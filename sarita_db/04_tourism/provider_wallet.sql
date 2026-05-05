CREATE TABLE tourism.provider_wallet (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    provider_id UUID NOT NULL, -- FK en 20_global
    wallet_id UUID NOT NULL,   -- FK en 20_global
    tipo_wallet TEXT DEFAULT 'comercial',

    created_at TIMESTAMP DEFAULT now()
);
