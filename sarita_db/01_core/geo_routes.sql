CREATE TABLE core.geo_routes_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    resource_id UUID NOT NULL,
    geo_path GEOGRAPHY(LineString, 4326) NOT NULL,

    started_at TIMESTAMP,
    ended_at TIMESTAMP
);
