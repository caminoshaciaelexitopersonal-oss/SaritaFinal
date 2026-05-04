-- Gestión Contable: Asientos Contables
CREATE TABLE core.journal_entries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operation_id UUID NOT NULL, -- FK en 20_global

    fecha DATE DEFAULT CURRENT_DATE,
    descripcion TEXT,

    created_at TIMESTAMP DEFAULT now()
);
