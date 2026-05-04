-- Historial Geográfico del Turista
CREATE TABLE tourism.tourist_geo_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL,
    geo_point GEOGRAPHY(Point, 4326) NOT NULL,
    context TEXT, -- busqueda, compra, navegacion, checkin

    created_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_tourist_geo_hist ON tourism.tourist_geo_history USING GIST(geo_point);
