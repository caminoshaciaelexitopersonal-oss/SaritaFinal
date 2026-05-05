-- Órdenes de Servicio (Núcleo Operativo)
CREATE TABLE core.service_orders_erp (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operation_id UUID NOT NULL, -- Vinculación con núcleo transaccional (30_mi_negocio)

    status TEXT DEFAULT 'pendiente', -- pendiente, en_proceso, completada, cancelada
    priority INT DEFAULT 3,

    scheduled_at TIMESTAMP,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
