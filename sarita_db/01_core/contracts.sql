-- Gestión Comercial: Contratos
CREATE TABLE core.contracts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    cliente_id UUID NOT NULL, -- FK en 20_global
    provider_id UUID NOT NULL, -- FK en 20_global

    fecha_inicio DATE NOT NULL,
    fecha_fin DATE,
    valor DECIMAL(18,2) NOT NULL,
    estado TEXT DEFAULT 'activo',

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
