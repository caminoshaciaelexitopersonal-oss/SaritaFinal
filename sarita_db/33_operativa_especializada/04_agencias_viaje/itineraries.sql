CREATE TABLE tourism.package_itineraries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    package_id UUID NOT NULL,
    day_number INT NOT NULL,

    activity_description TEXT NOT NULL,
    included_services JSONB DEFAULT '[]',

    created_at TIMESTAMP DEFAULT now()
);
