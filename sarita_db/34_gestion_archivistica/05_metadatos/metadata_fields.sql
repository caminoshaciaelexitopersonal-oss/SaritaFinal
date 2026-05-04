CREATE TABLE archival.metadata_fields (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    schema_id UUID NOT NULL,
    field_name TEXT NOT NULL,
    field_type TEXT NOT NULL, -- string, date, number, boolean

    is_required BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT now()
);
