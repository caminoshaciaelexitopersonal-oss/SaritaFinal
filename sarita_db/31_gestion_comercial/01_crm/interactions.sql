CREATE TABLE core.crm_interactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    customer_id UUID, -- Opcional si es lead
    lead_id UUID,

    type TEXT NOT NULL, -- call, email, chat, meeting
    content TEXT,
    sentiment_score DECIMAL(3,2),

    created_at TIMESTAMP DEFAULT now()
);
