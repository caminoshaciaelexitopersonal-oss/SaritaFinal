CREATE TABLE accounting.bank_movements_erp (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    bank_account_id UUID NOT NULL,
    movement_date DATE NOT NULL,
    amount DECIMAL(18,2) NOT NULL,

    reference TEXT,
    description TEXT,

    is_reconciled BOOLEAN DEFAULT false,

    created_at TIMESTAMP DEFAULT now()
);
