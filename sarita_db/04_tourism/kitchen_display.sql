CREATE TABLE tourism.kitchen_display_log (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    kitchen_order_id UUID NOT NULL,
    item_id UUID NOT NULL,

    action TEXT NOT NULL, -- start_prep, finish_prep
    timestamp TIMESTAMP DEFAULT now()
);
