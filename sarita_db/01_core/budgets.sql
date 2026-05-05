-- Presupuestos: Planificación Financiera
CREATE TABLE core.budgets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,
    version INT DEFAULT 1,

    name TEXT NOT NULL,
    period_start DATE NOT NULL,
    period_end DATE NOT NULL,

    status TEXT DEFAULT 'borrador', -- borrador, aprobado, ejecutando, cerrado
    total_planned DECIMAL(18,2) DEFAULT 0.00,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
