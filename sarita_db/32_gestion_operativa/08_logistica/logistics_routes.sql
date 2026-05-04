CREATE TABLE core.logistics_routes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT NOT NULL,
    geo_path GEOGRAPHY(LineString, 4326),

    estimated_duration_mins INT,

    created_at TIMESTAMP DEFAULT now()
);
