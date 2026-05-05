-- Flujo de Caja: Ejecución Real
CREATE TABLE core.cash_flow_actuals (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    actual_date DATE DEFAULT CURRENT_DATE,
    amount DECIMAL(18,2) NOT NULL,

    source_type TEXT NOT NULL, -- ledger, payment, transfer
    source_reference_id UUID,

    created_at TIMESTAMP DEFAULT now()
);
