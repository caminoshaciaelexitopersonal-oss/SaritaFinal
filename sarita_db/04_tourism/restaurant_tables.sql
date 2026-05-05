-- Especialización: Restaurantes
CREATE TABLE tourism.restaurant_tables (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operational_unit_id UUID NOT NULL,
    table_number TEXT NOT NULL,
    capacity INT DEFAULT 2,

    status TEXT DEFAULT 'libre', -- libre, ocupada, reservada

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
