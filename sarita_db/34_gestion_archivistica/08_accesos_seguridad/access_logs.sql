CREATE TABLE archival.document_access_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    document_id UUID NOT NULL,
    user_id UUID NOT NULL,

    access_type TEXT NOT NULL, -- read, download, print
    ip_address INET,

    accessed_at TIMESTAMP DEFAULT now()
);
