CREATE TABLE core.social_messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    conversation_id UUID NOT NULL, -- FK en 20_global
    sender_handle TEXT NOT NULL,
    message_text TEXT NOT NULL,

    is_from_me BOOLEAN DEFAULT false,
    external_msg_id TEXT,

    created_at TIMESTAMP DEFAULT now()
);
