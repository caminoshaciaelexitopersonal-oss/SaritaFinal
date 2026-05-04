CREATE TABLE archival.document_metadata_values (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    document_id UUID NOT NULL,
    field_id UUID NOT NULL,

    field_value TEXT,

    updated_at TIMESTAMP DEFAULT now()
);
