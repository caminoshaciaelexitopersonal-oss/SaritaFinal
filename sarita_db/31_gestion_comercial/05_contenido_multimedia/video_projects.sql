CREATE TABLE core.video_projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'borrador', -- borrador, editando, renderizando, completado

    product_id UUID, -- Opcional, vinculación con producto

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
