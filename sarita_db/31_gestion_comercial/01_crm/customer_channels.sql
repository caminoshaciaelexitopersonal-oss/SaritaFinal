CREATE TABLE core.customer_channels (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    customer_id UUID NOT NULL, -- FK en 20_global
    channel_type TEXT NOT NULL, -- whatsapp, instagram, telegram, email
    channel_identifier TEXT NOT NULL, -- numero, handle, email
    is_verified BOOLEAN DEFAULT false,

    created_at TIMESTAMP DEFAULT now(),
    UNIQUE(tenant_id, channel_type, channel_identifier)
);
