-- Flujo de Caja: Brechas (Gaps)
CREATE TABLE core.cash_flow_gaps (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    period_date DATE NOT NULL,
    net_position DECIMAL(18,2) NOT NULL,
    gap_status TEXT NOT NULL, -- superavit, deficit, critico

    suggested_action TEXT, -- solicitar_credito, adelantar_cobro

    measured_at TIMESTAMP DEFAULT now()
);
