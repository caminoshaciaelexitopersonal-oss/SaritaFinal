-- OCR y Extracción
CREATE TABLE archival.ocr_jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    version_id UUID NOT NULL,
    status TEXT DEFAULT 'pendiente', -- pendiente, procesando, completado, fallido

    started_at TIMESTAMP,
    completed_at TIMESTAMP,

    created_at TIMESTAMP DEFAULT now()
);
