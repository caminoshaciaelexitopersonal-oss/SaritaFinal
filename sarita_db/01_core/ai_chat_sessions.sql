CREATE TABLE core.ai_chat_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    customer_id UUID,
    lead_id UUID,

    external_convo_id TEXT, -- Vinculación con social_conversations
    current_intent TEXT,

    metadata JSONB DEFAULT '{}',

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
