-- Especialización: Guías Turísticos
CREATE TABLE tourism.guide_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL UNIQUE,
    rnt_number TEXT,
    languages JSONB DEFAULT '["español"]',
    specialties JSONB DEFAULT '[]',

    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT now()
);
