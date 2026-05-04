-- Control de Privacidad Geográfica
CREATE TABLE tourism.tourist_geo_consent (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL UNIQUE,
    consent_tracking BOOLEAN DEFAULT false,
    precision_level TEXT DEFAULT 'approx', -- exact, approx, off

    updated_at TIMESTAMP DEFAULT now()
);
