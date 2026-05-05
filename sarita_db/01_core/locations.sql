-- Geolocalización
CREATE TABLE core.operational_locations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT NOT NULL,
    location_type TEXT, -- parada, interes, peligro

    geo_point GEOGRAPHY(Point, 4326),

    created_at TIMESTAMP DEFAULT now()
);
