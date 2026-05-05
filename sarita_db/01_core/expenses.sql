-- Gestión de Gastos (Complemento de Ledger y Contable)
CREATE TABLE core.financial_expenses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    expense_type TEXT NOT NULL, -- operativo, nomina, marketing, servicios_publicos
    category TEXT,

    provider_name TEXT, -- Opcional, puede ser FK a providers
    amount DECIMAL(18,2) NOT NULL,

    status TEXT DEFAULT 'pendiente', -- pendiente, aprobado, pagado, rechazado

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
