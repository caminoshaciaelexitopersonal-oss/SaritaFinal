CREATE TABLE kyc.kyc_verifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    kyc_profile_id UUID NOT NULL, -- FK in 20_global
    verifier_id UUID, -- FK in 20_global
    verification_type VARCHAR(50) NOT NULL,
    result VARCHAR(20) NOT NULL, -- APPROVED, REJECTED
    notes TEXT,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
