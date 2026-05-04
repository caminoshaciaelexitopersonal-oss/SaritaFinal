-- Financiamiento: Pagos de Cuotas
CREATE TABLE core.loan_payments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    loan_id UUID NOT NULL,
    installment_number INT NOT NULL,

    principal_paid DECIMAL(18,2) NOT NULL,
    interest_paid DECIMAL(18,2) NOT NULL,
    other_fees DECIMAL(18,2) DEFAULT 0.00,

    status TEXT DEFAULT 'pagado',
    paid_at TIMESTAMP DEFAULT now()
);
