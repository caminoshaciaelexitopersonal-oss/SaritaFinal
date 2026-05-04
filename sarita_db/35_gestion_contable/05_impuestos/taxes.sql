-- Impuestos (Traducción de Tax)
CREATE TABLE accounting.taxes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    code VARCHAR(50) NOT NULL,
    name TEXT NOT NULL,
    tax_type TEXT NOT NULL, -- IVA, RET, ISR, ICA

    is_deductible BOOLEAN DEFAULT false,
    is_withholding BOOLEAN DEFAULT false,

    active BOOLEAN DEFAULT true,
    effective_from DATE NOT NULL,
    effective_to DATE,

    created_at TIMESTAMP DEFAULT now(),
    UNIQUE(tenant_id, code)
);
