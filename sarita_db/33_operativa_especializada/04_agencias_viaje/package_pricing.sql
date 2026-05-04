CREATE TABLE tourism.package_pricing (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    package_id UUID NOT NULL,
    person_type TEXT NOT NULL, -- Adulto, Niño, Infante
    price DECIMAL(18,2) NOT NULL,

    created_at TIMESTAMP DEFAULT now()
);
