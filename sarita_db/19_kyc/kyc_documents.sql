CREATE TABLE kyc.kyc_documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    kyc_profile_id UUID NOT NULL, -- FK in 20_global
    document_type VARCHAR(50) NOT NULL,
    document_hash TEXT NOT NULL,
    storage_ref TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'PENDING',
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
