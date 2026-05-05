CREATE TABLE core.social_post_queue (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    account_id UUID NOT NULL,
    post_id UUID NOT NULL,

    scheduled_at TIMESTAMP NOT NULL,
    published_at TIMESTAMP,
    status TEXT DEFAULT 'pendiente', -- pendiente, publicado, fallido

    created_at TIMESTAMP DEFAULT now()
);
