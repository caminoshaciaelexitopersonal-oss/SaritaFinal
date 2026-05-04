CREATE TABLE core.social_conversations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    account_id UUID NOT NULL,
    external_convo_id TEXT NOT NULL,
    participant_handle TEXT NOT NULL,

    customer_id UUID, -- Vinculación con CRM si existe

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
