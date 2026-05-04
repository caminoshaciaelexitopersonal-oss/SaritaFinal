CREATE TABLE core.logistics_assignments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    logistics_order_id UUID NOT NULL,
    resource_id UUID NOT NULL, -- Vehículo o Persona

    assigned_at TIMESTAMP DEFAULT now()
);
