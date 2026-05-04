-- Analítica Financiera: Métricas
CREATE TABLE core.financial_metrics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    periodo_inicio DATE NOT NULL,
    periodo_fin DATE NOT NULL,

    ingresos DECIMAL(18,2) DEFAULT 0.00,
    costos DECIMAL(18,2) DEFAULT 0.00,
    utilidad DECIMAL(18,2) DEFAULT 0.00,
    margen DECIMAL(5,2) DEFAULT 0.00,

    created_at TIMESTAMP DEFAULT now()
);
