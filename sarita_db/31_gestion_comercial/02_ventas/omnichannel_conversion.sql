CREATE TABLE core.omnichannel_conversion (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    source_channel TEXT NOT NULL, -- whatsapp, ig, web
    campaign_id UUID,             -- FK en 20_global
    product_id UUID,              -- FK en 20_global

    ai_involved BOOLEAN DEFAULT false,
    conversion_value DECIMAL(18,2) DEFAULT 0.00,

    created_at TIMESTAMP DEFAULT now()
);
