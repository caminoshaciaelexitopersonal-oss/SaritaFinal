-- Talleres Físicos de Artesanos
CREATE TABLE tourism.artisan_workshops (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    artisan_id UUID NOT NULL,
    nombre TEXT NOT NULL,
    tipo_taller TEXT NOT NULL, -- taller_productivo, punto_venta, taller_movil

    capacidad_produccion INT,
    visitas_permitidas BOOLEAN DEFAULT false,

    geo_point GEOGRAPHY(Point, 4326),
    created_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_workshop_geo ON tourism.artisan_workshops USING GIST(geo_point);
