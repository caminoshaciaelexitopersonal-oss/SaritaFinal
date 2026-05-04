-- Vínculos de Transacción
CREATE TABLE accounting.transaction_links (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    journal_entry_id UUID NOT NULL,
    source_document_type TEXT NOT NULL, -- invoice, payment, payroll
    source_document_id UUID NOT NULL,

    created_at TIMESTAMP DEFAULT now()
);
