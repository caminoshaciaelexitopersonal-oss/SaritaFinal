CREATE TABLE core.automation_actions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    rule_id UUID NOT NULL, -- FK en 20_global
    action_type TEXT NOT NULL, -- send_message, notify_agent, update_lead
    action_config JSONB NOT NULL,

    order_index INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT now()
);
