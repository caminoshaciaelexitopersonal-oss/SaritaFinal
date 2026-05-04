-- Firma Electrónica: Firmas (Metadata Legal)
CREATE TABLE archival.signatures (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    participant_id UUID NOT NULL,
    signature_value TEXT NOT NULL, -- PKI, Biométrico o Hash

    verification_metadata JSONB,

    created_at TIMESTAMP DEFAULT now()
);
