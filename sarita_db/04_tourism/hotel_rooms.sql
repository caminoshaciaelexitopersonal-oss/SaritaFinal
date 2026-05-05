-- Especialización: Hoteles
CREATE TABLE tourism.hotel_rooms (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operational_unit_id UUID NOT NULL, -- Sede del hotel
    room_number TEXT NOT NULL,
    room_type_id UUID NOT NULL, -- Ref a room_types

    status TEXT DEFAULT 'disponible', -- disponible, ocupada, limpieza, mantenimiento

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
