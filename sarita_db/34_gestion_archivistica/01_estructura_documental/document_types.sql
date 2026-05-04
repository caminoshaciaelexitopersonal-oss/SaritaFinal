CREATE TABLE archival.document_types_extended (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    category_id UUID NOT NULL, -- FK en 20_global
    name TEXT NOT NULL, -- Contrato, Factura, Acta, etc.
    code VARCHAR(10) UNIQUE,

    created_at TIMESTAMP DEFAULT now()
);
