CREATE TABLE IF NOT EXISTS finance.payment_intents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    amount NUMERIC NOT NULL, status TEXT
    CONSTRAINT unq_payment_trace UNIQUE (trace_id),
    context_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
