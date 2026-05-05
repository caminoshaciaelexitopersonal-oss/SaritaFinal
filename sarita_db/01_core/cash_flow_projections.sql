-- Flujo de Caja: Proyecciones
CREATE TABLE core.cash_flow_projections (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    projection_date DATE NOT NULL,
    flow_type TEXT NOT NULL, -- entrada, salida
    estimated_amount DECIMAL(18,2) NOT NULL,
    probability DECIMAL(3,2) DEFAULT 1.00, -- 0.00 a 1.00

    source TEXT, -- lead_potential, contract, subscription

    created_at TIMESTAMP DEFAULT now()
);
