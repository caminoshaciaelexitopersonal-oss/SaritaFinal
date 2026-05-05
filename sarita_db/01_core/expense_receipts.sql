CREATE TABLE core.expense_receipts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    expense_id UUID NOT NULL,
    document_url TEXT NOT NULL, -- Ref a 34_archivística

    ocr_status TEXT DEFAULT 'no_iniciado', -- pendiente, completado, error
    validation_status TEXT DEFAULT 'pendiente',

    created_at TIMESTAMP DEFAULT now()
);
