CREATE TABLE tourism.room_inventory (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    room_id UUID NOT NULL,
    item_name TEXT NOT NULL, -- Toallas, Jabón, Almohadas
    quantity INT DEFAULT 0,

    updated_at TIMESTAMP DEFAULT now()
);
