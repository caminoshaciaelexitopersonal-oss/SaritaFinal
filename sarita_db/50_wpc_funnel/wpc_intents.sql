-- WPC Intents (La única forma en que el frontend interactúa)
CREATE TABLE core.wpc_intents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    session_id UUID NOT NULL, -- FK en 20_global
    intent_type TEXT NOT NULL, -- compra, reserva, cotizacion

    payload JSONB NOT NULL, -- producto_id, cantidad, fechas, etc.
    status TEXT DEFAULT 'pendiente', -- pendiente, procesando, completado, fallido

    error_message TEXT,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
