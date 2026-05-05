CREATE TABLE core.ai_response_templates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    intent_id UUID NOT NULL, -- FK en 20_global
    template_text TEXT NOT NULL,
    language TEXT DEFAULT 'es',

    created_at TIMESTAMP DEFAULT now()
);
