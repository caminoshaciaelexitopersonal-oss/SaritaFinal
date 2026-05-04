-- Geolocalización de Artesanos (Nivel Profesional)
CREATE TABLE tourism.artisan_locations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    artisan_id UUID NOT NULL,
    pais TEXT DEFAULT 'Colombia',
    departamento TEXT,
    municipio TEXT,
    direccion TEXT,

    geo_point GEOGRAPHY(Point, 4326) NOT NULL,
    precision_geo TEXT DEFAULT 'alta', -- alta, media, baja

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_artisan_geo ON tourism.artisan_locations USING GIST(geo_point);
