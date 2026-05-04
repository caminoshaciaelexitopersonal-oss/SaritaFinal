CREATE TABLE archival.export_files (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    job_id UUID NOT NULL,
    file_url TEXT NOT NULL,

    expires_at TIMESTAMP,

    created_at TIMESTAMP DEFAULT now()
);
