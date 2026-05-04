-- Especialización: Agencias de Viaje
CREATE TABLE tourism.travel_packages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    provider_id UUID NOT NULL,
    name TEXT NOT NULL,
    description TEXT,

    total_price DECIMAL(18,2),
    is_published BOOLEAN DEFAULT false,

    created_at TIMESTAMP DEFAULT now()
);
