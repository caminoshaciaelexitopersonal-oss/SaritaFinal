-- Directorio: Índice de Búsqueda Avanzada
CREATE TABLE tourism.artisan_directory_index (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    artisan_id UUID NOT NULL UNIQUE,
    nombre_busqueda TEXT NOT NULL,
    categoria_nombre TEXT,

    geo_point GEOGRAPHY(Point, 4326),
    rating_promedio DECIMAL(3,2) DEFAULT 0.00,
    popularidad_score INT DEFAULT 0,

    searchable_vector tsvector,
    last_sync TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_artisan_dir_geo ON tourism.artisan_directory_index USING GIST(geo_point);
CREATE INDEX idx_artisan_dir_search ON tourism.artisan_directory_index USING GIN(searchable_vector);
