-- Sesiones del Turista (WPC Side)
CREATE TABLE core.tourist_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL UNIQUE,
    hash_integridad TEXT,

    user_id UUID NOT NULL,
    session_status TEXT DEFAULT 'activa', -- activa, abandonada, convertida
    channel TEXT NOT NULL, -- web, voz, app

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
