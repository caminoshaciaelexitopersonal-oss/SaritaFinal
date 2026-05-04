-- Operativa Especializada: Asignación de Recursos
CREATE TABLE core.resource_allocation (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    service_order_id UUID NOT NULL, -- FK en 20_global

    tipo_recurso TEXT NOT NULL,
    recurso_id UUID NOT NULL, -- Ref genérica a tabla de recursos
    cantidad INT DEFAULT 1,

    created_at TIMESTAMP DEFAULT now()
);
