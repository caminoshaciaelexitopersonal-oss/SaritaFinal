CREATE TABLE payments.payment_settlements (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    payment_intent_id UUID NOT NULL, -- FK in 20_global
    amount_settled DECIMAL(18,2) NOT NULL,
    settled_at TIMESTAMPTZ DEFAULT now(),
    reference VARCHAR(255),
    tenant_id UUID NOT NULL,
    hash_integridad TEXT
);
