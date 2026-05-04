CREATE TABLE core.media_storage_metadata (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    asset_id UUID NOT NULL, -- FK en 20_global
    storage_provider TEXT DEFAULT 'local', -- AWS S3, Google Cloud, IPFS
    physical_path TEXT NOT NULL,
    cdn_url TEXT,

    created_at TIMESTAMP DEFAULT now()
);
