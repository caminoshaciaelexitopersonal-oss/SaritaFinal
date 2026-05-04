CREATE TABLE tourism.association_shared_services (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    association_id UUID NOT NULL,
    service_catalog_id UUID NOT NULL, -- Ref a genérico

    commission_percentage DECIMAL(5,2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT now()
);
