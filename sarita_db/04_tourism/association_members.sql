-- Especialización: Asociaciones de Guías
CREATE TABLE tourism.association_members (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    association_id UUID NOT NULL, -- Ref a tourism_providers
    guide_user_id UUID NOT NULL,

    membership_status TEXT DEFAULT 'activo',
    joined_at DATE DEFAULT CURRENT_DATE
);
