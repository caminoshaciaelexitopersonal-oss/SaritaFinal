-- Tesorería: Transferencias Internas
CREATE TABLE core.cash_transfers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,
    version INT DEFAULT 1,

    source_account_id UUID NOT NULL,
    destination_account_id UUID NOT NULL,

    amount DECIMAL(18,2) NOT NULL,
    status TEXT DEFAULT 'completada',

    executed_at TIMESTAMP DEFAULT now()
);
