CREATE TABLE archival.document_notarizations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    document_id UUID NOT NULL,
    notary_id UUID NOT NULL,
    notarization_hash TEXT NOT NULL,
    notarization_date TIMESTAMPTZ DEFAULT now(),
    tenant_id UUID NOT NULL,
    hash_integridad TEXT
);
