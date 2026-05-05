-- Especialización: Bares / Discotecas
CREATE TABLE tourism.establishment_zones (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operational_unit_id UUID NOT NULL,
    name TEXT NOT NULL, -- VIP, Barra, Terraza

    capacity INT NOT NULL,
    created_at TIMESTAMP DEFAULT now()
);
