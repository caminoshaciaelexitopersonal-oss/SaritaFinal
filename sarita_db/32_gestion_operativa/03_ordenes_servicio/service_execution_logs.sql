CREATE TABLE core.service_execution_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    service_order_id UUID NOT NULL,
    actor_id UUID NOT NULL, -- Usuario que ejecuta

    action TEXT NOT NULL,
    observations TEXT,

    executed_at TIMESTAMP DEFAULT now()
);
