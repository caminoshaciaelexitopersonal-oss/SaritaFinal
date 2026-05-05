CREATE TABLE tourism.guide_certifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    guide_id UUID NOT NULL,
    cert_name TEXT NOT NULL,
    expiry_date DATE,

    created_at TIMESTAMP DEFAULT now()
);
