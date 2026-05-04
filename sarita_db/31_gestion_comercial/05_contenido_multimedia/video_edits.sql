CREATE TABLE core.video_edits (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    project_id UUID NOT NULL, -- FK en 20_global
    edit_payload JSONB NOT NULL, -- Timeline, cuts, filters
    version INT DEFAULT 1,

    author_id UUID NOT NULL,  -- FK a users

    created_at TIMESTAMP DEFAULT now()
);
