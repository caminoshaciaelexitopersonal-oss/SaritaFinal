-- Analítica: Centros de Costo
CREATE TABLE accounting.cost_centers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    code VARCHAR(20) NOT NULL,
    name TEXT NOT NULL,

    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT now(),
    UNIQUE(tenant_id, code)
);
