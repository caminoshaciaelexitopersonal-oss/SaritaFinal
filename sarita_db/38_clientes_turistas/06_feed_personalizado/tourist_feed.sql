-- Feed Personalizado (El Home Inteligente)
CREATE TABLE core.tourist_feed (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL,
    content_type TEXT NOT NULL, -- evento, producto, ruta, noticia
    content_id UUID NOT NULL,

    relevance_score DECIMAL(5,2),
    expiry_date TIMESTAMP,

    created_at TIMESTAMP DEFAULT now()
);
