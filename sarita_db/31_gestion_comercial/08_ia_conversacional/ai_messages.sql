CREATE TABLE core.ai_chat_messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    session_id UUID NOT NULL, -- FK en 20_global
    message_text TEXT NOT NULL,
    role TEXT NOT NULL, -- user, assistant, system

    tokens_count INT,
    model_version TEXT,

    created_at TIMESTAMP DEFAULT now()
);
