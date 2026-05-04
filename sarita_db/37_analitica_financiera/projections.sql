-- Analítica Financiera: Proyecciones
CREATE TABLE core.financial_projections (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    periodo VARCHAR(50) NOT NULL, -- Q1-2026, etc.
    flujo_estimado DECIMAL(18,2),
    riesgo TEXT, -- BAJO, MEDIO, ALTO

    created_at TIMESTAMP DEFAULT now()
);
