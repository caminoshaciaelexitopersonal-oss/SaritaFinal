-- Reglas de Impuesto (Traducción de TaxRule)
CREATE TABLE accounting.tax_rules_contable (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    tax_id UUID NOT NULL,
    document_type TEXT NOT NULL,
    entity_type TEXT NOT NULL,

    minimum_base DECIMAL(18,2) DEFAULT 0,
    maximum_base DECIMAL(18,2),

    condition_expression TEXT,
    priority INT DEFAULT 0,

    created_at TIMESTAMP DEFAULT now()
);
