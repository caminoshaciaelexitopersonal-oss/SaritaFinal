CREATE TABLE tourism.guide_services (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    guide_id UUID NOT NULL,
    service_name TEXT NOT NULL,
    hourly_rate DECIMAL(18,2),

    created_at TIMESTAMP DEFAULT now()
);
