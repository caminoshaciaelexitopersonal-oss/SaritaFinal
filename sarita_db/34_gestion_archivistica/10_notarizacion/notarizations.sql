CREATE TABLE archival.notarizations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    document_version_id UUID NOT NULL,
    provider_id UUID NOT NULL,

    external_reference_id TEXT, -- TxHash, ID de acta
    notarization_hash TEXT NOT NULL,

    timestamp TIMESTAMP DEFAULT now()
);
