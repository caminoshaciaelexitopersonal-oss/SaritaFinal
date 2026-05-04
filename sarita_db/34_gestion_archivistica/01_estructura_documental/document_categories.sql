-- Estructura Documental: Categorías
CREATE TABLE archival.document_categories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT NOT NULL, -- Legal, Contable, Operativo, SST
    description TEXT,

    created_at TIMESTAMP DEFAULT now()
);
