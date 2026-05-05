CREATE TABLE tourism.multi_provider_orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    main_operation_id UUID NOT NULL,
    sub_provider_id UUID NOT NULL,

    status TEXT DEFAULT 'pendiente',
    created_at TIMESTAMP DEFAULT now()
);
