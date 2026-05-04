CREATE TABLE core.geo_points_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    resource_id UUID NOT NULL, -- GPS de vehiculo o persona
    geo_point GEOGRAPHY(Point, 4326) NOT NULL,

    measured_at TIMESTAMP DEFAULT now()
);
