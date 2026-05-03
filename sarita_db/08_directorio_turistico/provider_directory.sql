-- Directorio Turístico de Prestadores
CREATE TABLE tourism.provider_directory (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    provider_id UUID NOT NULL, -- FK en 20_global

    categoria TEXT NOT NULL,
    subcategoria TEXT,
    descripcion_publica TEXT,

    imagenes JSONB DEFAULT '[]',
    horarios JSONB DEFAULT '{}',

    precio_rango TEXT, -- $, $$, $$$
    idiomas JSONB DEFAULT '["español"]',
    accesibilidad JSONB DEFAULT '[]',

    searchable_vector tsvector,
    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);

-- Trigger para vector de búsqueda (simplificado)
CREATE TRIGGER trg_provider_tsvector BEFORE INSERT OR UPDATE ON tourism.provider_directory
FOR EACH ROW EXECUTE PROCEDURE tsvector_update_trigger(searchable_vector, 'pg_catalog.spanish', categoria, subcategoria, descripcion_publica);
