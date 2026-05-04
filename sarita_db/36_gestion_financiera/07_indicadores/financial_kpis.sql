-- Indicadores Financieros (Analítica)
CREATE TABLE core.financial_kpis (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    kpi_name TEXT NOT NULL, -- liquidez, solvencia, rentabilidad
    current_value DECIMAL(18,4),
    target_value DECIMAL(18,4),

    status TEXT, -- OPTIMO, ALERTA, CRITICO
    measured_at TIMESTAMP DEFAULT now()
);
