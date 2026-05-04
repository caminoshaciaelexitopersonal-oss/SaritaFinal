-- Recursos (Gente, Equipos, Vehículos)
CREATE TABLE core.operational_resources (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    resource_name TEXT NOT NULL,
    resource_type_id UUID NOT NULL, -- FK en 20_global

    metadata JSONB DEFAULT '{}',
    is_active BOOLEAN DEFAULT true,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
