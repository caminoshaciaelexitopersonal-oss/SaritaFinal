CREATE TABLE core.checklist_execution (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    checklist_id UUID NOT NULL,
    service_order_id UUID,
    actor_id UUID NOT NULL,

    results JSONB NOT NULL, -- {item_id: ok/fail}
    observations TEXT,

    executed_at TIMESTAMP DEFAULT now()
);
