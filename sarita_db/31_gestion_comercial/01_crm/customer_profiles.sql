CREATE TABLE core.customer_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    customer_id UUID NOT NULL, -- FK en 20_global
    preferences JSONB DEFAULT '{}',
    demographics JSONB DEFAULT '{}',
    acquisition_channel TEXT,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
