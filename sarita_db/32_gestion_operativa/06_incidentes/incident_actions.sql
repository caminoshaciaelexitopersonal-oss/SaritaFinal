CREATE TABLE core.incident_actions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    incident_id UUID NOT NULL,
    action_description TEXT NOT NULL,
    actor_id UUID NOT NULL,

    executed_at TIMESTAMP DEFAULT now()
);
