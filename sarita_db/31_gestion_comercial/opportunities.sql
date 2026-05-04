-- Gestión Comercial: Oportunidades
CREATE TYPE core.opportunity_status AS ENUM ('lead', 'prospecto', 'cerrado');

CREATE TABLE core.opportunities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    cliente_id UUID NOT NULL, -- FK en 20_global
    estado core.opportunity_status DEFAULT 'lead',

    valor_estimado DECIMAL(18,2) DEFAULT 0.00,
    probabilidad INT CHECK (probabilidad BETWEEN 0 AND 100),

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
