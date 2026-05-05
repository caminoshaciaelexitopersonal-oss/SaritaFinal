CREATE TABLE tourism.menus (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    provider_id UUID NOT NULL,
    name TEXT NOT NULL, -- Menu Ejecutivo, Carta, Bebidas

    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT now()
);
