-- Logs de Recomendaciones (IA Tracking)
CREATE TABLE core.tourist_recommendation_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL,
    recommendation_payload JSONB NOT NULL,

    action_taken TEXT DEFAULT 'mostrada', -- mostrada, aceptada, ignorada
    conversion_id UUID, -- Si aceptó y compró

    created_at TIMESTAMP DEFAULT now()
);
