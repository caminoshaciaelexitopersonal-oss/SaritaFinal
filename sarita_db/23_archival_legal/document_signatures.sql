CREATE TABLE archival.document_signatures (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    document_id UUID NOT NULL,
    signer_id UUID NOT NULL, -- FK in 20_global
    signature_hash TEXT NOT NULL,
    signature_metadata JSONB DEFAULT '{}',
    signed_at TIMESTAMPTZ DEFAULT now(),
    tenant_id UUID NOT NULL,
    hash_integridad TEXT
);
