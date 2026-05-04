-- Referencias Transaccionales del Turista (NO duplicación)
CREATE TABLE core.tourist_transaction_refs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL,
    transaction_id UUID, -- Ref a ledger.transactions / payments
    booking_id UUID,     -- Ref a core.bookings_erp / service_orders

    source_domain TEXT NOT NULL, -- 'payments', 'reservas', 'citas'
    created_at TIMESTAMP DEFAULT now()
);
