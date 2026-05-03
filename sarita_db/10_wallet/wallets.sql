CREATE TABLE wallet.wallets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    owner_id UUID NOT NULL REFERENCES identity.users(id),
    balance DECIMAL(18,2) DEFAULT 0.00,
    currency VARCHAR(3) DEFAULT 'COP',
    status VARCHAR(20) DEFAULT 'ACTIVE',
    tenant_id UUID REFERENCES core.tenants(id),
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
