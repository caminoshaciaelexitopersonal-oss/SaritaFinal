CREATE TABLE core.funnel_tracking (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    lead_id UUID NOT NULL, -- FK en 20_global
    funnel_step_id UUID NOT NULL, -- FK en 20_global

    entered_at TIMESTAMP DEFAULT now(),
    exited_at TIMESTAMP,
    status TEXT DEFAULT 'active' -- active, converted, dropped
);
