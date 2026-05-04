-- Gestión Contable: Líneas de Asiento (Doble Entrada)
CREATE TABLE core.journal_lines (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    journal_entry_id UUID NOT NULL, -- FK en 20_global

    cuenta_id UUID NOT NULL, -- FK en 20_global (PUC)
    debito DECIMAL(18,2) DEFAULT 0.00,
    credito DECIMAL(18,2) DEFAULT 0.00,

    created_at TIMESTAMP DEFAULT now(),

    CONSTRAINT chk_journal_line CHECK ((debito > 0 AND credito = 0) OR (credito > 0 AND debito = 0))
);
