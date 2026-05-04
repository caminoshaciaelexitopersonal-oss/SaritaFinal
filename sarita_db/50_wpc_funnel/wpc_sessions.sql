-- WPC Sessions (Frontend/Funnel Side)
CREATE TABLE core.wpc_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL UNIQUE,
    hash_integridad TEXT,

    user_id UUID NOT NULL, -- FK en 20_global
    status TEXT DEFAULT 'activo', -- activo, abandonado, convertido
    channel TEXT NOT NULL, -- web, voz, app

    metadata JSONB DEFAULT '{}',

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
