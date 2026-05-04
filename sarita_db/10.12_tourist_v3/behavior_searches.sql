-- 02_identity/tourist_searches.sql
-- Registro de búsquedas para motor de recomendaciones
CREATE TABLE IF NOT EXISTS identity.tourist_searches (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tourist_id UUID NOT NULL REFERENCES identity.tourist_profiles(id),
    query TEXT,
    filters JSONB DEFAULT '{}', -- Categorías, rangos de precio, etc.
    results_count INTEGER DEFAULT 0,
    clicked_id UUID, -- Si hizo click en algún resultado (provider_id o product_id)
    device_info JSONB,
    location_context GEOGRAPHY(POINT, 4326), -- Desde dónde buscaba
    tenant_id UUID NOT NULL,
    trace_id UUID,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

CREATE INDEX idx_tourist_searches_tourist ON identity.tourist_searches(tourist_id);
CREATE INDEX idx_tourist_searches_filters ON identity.tourist_searches USING GIN (filters);
CREATE INDEX idx_tourist_searches_tenant ON identity.tourist_searches(tenant_id);
