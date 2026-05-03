CREATE TABLE kyc.kyc_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL, -- FK in 20_global
    status VARCHAR(20) DEFAULT 'PENDING',
    risk_score INTEGER DEFAULT 0,
    verification_data JSONB DEFAULT '{}',
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
