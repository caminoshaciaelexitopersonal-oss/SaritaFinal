-- Especialización: Transporte Turístico
CREATE TABLE tourism.operational_vehicles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    provider_id UUID NOT NULL,
    plate TEXT UNIQUE NOT NULL,
    vehicle_type_id UUID NOT NULL,

    status TEXT DEFAULT 'activo', -- activo, taller, fuera_servicio

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
