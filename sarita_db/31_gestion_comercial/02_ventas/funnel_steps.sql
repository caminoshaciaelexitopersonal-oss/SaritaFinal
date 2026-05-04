CREATE TABLE core.funnel_steps (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    funnel_id UUID NOT NULL, -- FK en 20_global
    step_name TEXT NOT NULL,
    order_index INT NOT NULL,
    expected_conversion_rate DECIMAL(5,2),

    created_at TIMESTAMP DEFAULT now()
);
