CREATE TABLE core.leads_erp (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    nombre TEXT NOT NULL,
    email CITEXT,
    telefono TEXT,
    source TEXT, -- web, whatsapp, ig, tiktok
    status TEXT DEFAULT 'nuevo',

    assigned_agent_id UUID, -- FK a users en 20_global

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
