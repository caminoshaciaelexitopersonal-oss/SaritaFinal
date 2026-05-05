-- Catálogo de Clientes (Vía 2/3)
CREATE TABLE core.customers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    nombre TEXT NOT NULL,
    tipo TEXT DEFAULT 'persona_natural', -- jurídica, natural
    email CITEXT UNIQUE,
    telefono TEXT,

    identificacion TEXT,
    direccion TEXT,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
