-- Periodos Contables (Traducción de FiscalPeriod)
CREATE TABLE accounting.fiscal_periods (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,

    is_closed BOOLEAN DEFAULT false,

    created_at TIMESTAMP DEFAULT now()
);
