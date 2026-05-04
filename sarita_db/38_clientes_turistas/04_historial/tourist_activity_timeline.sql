-- Timeline de Actividad del Turista
CREATE TABLE core.tourist_activity_timeline (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL,
    activity_type TEXT NOT NULL, -- view, click, search, buy, review
    reference_id UUID, -- Ref al objeto impactado

    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT now()
);
