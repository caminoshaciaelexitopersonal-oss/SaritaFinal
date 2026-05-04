-- Exportación y Auditoría
CREATE TABLE archival.export_jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    request_id UUID NOT NULL, -- Usuario solicitante
    status TEXT DEFAULT 'pendiente',

    format TEXT DEFAULT 'ZIP', -- PDF_CONCAT, ZIP

    started_at TIMESTAMP,
    completed_at TIMESTAMP,

    created_at TIMESTAMP DEFAULT now()
);
