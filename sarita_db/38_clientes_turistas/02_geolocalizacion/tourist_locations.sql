-- Geolocalización del Usuario (Tiempo Real)
CREATE TABLE tourism.tourist_locations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL UNIQUE,
    geo_point GEOGRAPHY(Point, 4326) NOT NULL,
    precision_meters DECIMAL(10,2),

    updated_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_tourist_geo ON tourism.tourist_locations USING GIST(geo_point);
