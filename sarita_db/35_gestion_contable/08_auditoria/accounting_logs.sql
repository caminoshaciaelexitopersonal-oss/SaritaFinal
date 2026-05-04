-- Auditoría Contable (Traducción de AccountingAuditLog)
CREATE TABLE accounting.accounting_audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL, -- FK a users
    action TEXT NOT NULL, -- POST, REVERSE, CLOSE_PERIOD

    reference_entry_id UUID, -- FK a journal_entries
    ip_address INET,
    integrity_hash VARCHAR(64),

    created_at TIMESTAMP DEFAULT now()
);
