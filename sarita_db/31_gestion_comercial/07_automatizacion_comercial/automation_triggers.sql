CREATE TABLE core.automation_triggers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    rule_id UUID NOT NULL, -- FK en 20_global
    event_type TEXT NOT NULL, -- message_received, lead_created, order_placed
    conditions_json JSONB DEFAULT '{}',

    created_at TIMESTAMP DEFAULT now()
);
