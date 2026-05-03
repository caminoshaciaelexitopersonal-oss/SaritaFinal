CREATE TABLE tourism.provider_structure (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    provider_id UUID NOT NULL, -- FK en 20_global
    parent_provider_id UUID,   -- FK en 20_global

    tipo_relacion TEXT NOT NULL, -- matriz, sucursal, franquicia, filial
    nivel INT DEFAULT 1,

    created_at TIMESTAMP DEFAULT now()
);
