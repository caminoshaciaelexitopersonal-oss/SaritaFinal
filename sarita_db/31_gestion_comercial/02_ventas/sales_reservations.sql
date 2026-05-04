-- Reservas Comerciales (Experiencias/Talleres)
CREATE TABLE core.sales_reservations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    user_id UUID NOT NULL,
    artisan_id UUID, -- O provider_id

    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,

    capacity_reserved INT DEFAULT 1,
    status TEXT DEFAULT 'pendiente', -- pendiente, confirmada, cancelada

    metadata JSONB DEFAULT '{}',

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
