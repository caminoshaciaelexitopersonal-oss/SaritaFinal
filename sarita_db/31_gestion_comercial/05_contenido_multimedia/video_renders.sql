CREATE TABLE core.video_renders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    project_id UUID NOT NULL, -- FK en 20_global
    resolution TEXT NOT NULL, -- 1080p, 4k
    format TEXT NOT NULL,     -- mp4, mov

    output_url TEXT NOT NULL,
    render_time_ms INT,

    created_at TIMESTAMP DEFAULT now()
);
