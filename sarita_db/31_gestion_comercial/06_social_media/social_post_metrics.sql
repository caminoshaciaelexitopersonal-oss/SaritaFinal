CREATE TABLE core.social_post_metrics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    post_id UUID NOT NULL,
    likes INT DEFAULT 0,
    shares INT DEFAULT 0,
    comments_count INT DEFAULT 0,
    reach INT DEFAULT 0,
    clicks INT DEFAULT 0,

    measured_at TIMESTAMP DEFAULT now()
);
