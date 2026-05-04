-- Configuración Contable
CREATE TABLE accounting.accounting_settings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    base_currency VARCHAR(3) DEFAULT 'COP',
    chained_hash_enabled BOOLEAN DEFAULT true,

    updated_at TIMESTAMP DEFAULT now()
);
