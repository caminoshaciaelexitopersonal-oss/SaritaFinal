CREATE TABLE kyc.kyc_risk_scores (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    kyc_profile_id UUID NOT NULL, -- FK in 20_global
    score INTEGER NOT NULL,
    factors JSONB DEFAULT '[]',
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
