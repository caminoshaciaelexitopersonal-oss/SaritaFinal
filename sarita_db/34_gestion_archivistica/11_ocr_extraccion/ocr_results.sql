CREATE TABLE archival.ocr_results (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    job_id UUID NOT NULL,
    extracted_text TEXT,

    raw_json JSONB, -- Coordinates, fonts, confidence per word

    created_at TIMESTAMP DEFAULT now()
);
