CREATE TABLE core.ai_conversion_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    session_id UUID NOT NULL,
    order_id UUID NOT NULL,

    value DECIMAL(18,2) NOT NULL,
    attribution_confidence DECIMAL(3,2) DEFAULT 1.00,

    created_at TIMESTAMP DEFAULT now()
);
