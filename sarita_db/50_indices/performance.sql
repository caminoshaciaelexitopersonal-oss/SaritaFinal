-- Índices de rendimiento avanzados - FASE V1-GOV

-- Índices geoespaciales para atractivos y eventos
CREATE INDEX IF NOT EXISTS idx_attractions_geo ON tourism.attractions USING GIST(location);
CREATE INDEX IF NOT EXISTS idx_events_geo ON tourism.events USING GIST(location);
CREATE INDEX IF NOT EXISTS idx_territorial_geo ON governance.territorial_entities USING GIST(location);

-- Índices de búsqueda textual para el directorio turístico
CREATE INDEX IF NOT EXISTS idx_directory_search ON tourism.tourism_directory USING GIN(searchable_vector);

-- Índices por código DANE y Tenant
CREATE INDEX IF NOT EXISTS idx_territorial_dane ON governance.territorial_entities (dane_code);
CREATE INDEX IF NOT EXISTS idx_public_entities_type ON governance.public_entities (entity_type);
