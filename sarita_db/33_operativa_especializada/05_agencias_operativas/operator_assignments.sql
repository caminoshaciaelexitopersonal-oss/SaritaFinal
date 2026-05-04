-- Especialización: Agencias Operativas
CREATE TABLE tourism.operator_assignments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    service_order_id UUID NOT NULL,
    operator_resource_id UUID NOT NULL, -- Ref a persona/guía

    assigned_at TIMESTAMP DEFAULT now()
);
