-- Control de Asistencia a Citas
CREATE TABLE core.appointment_attendance (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    booking_id UUID NOT NULL,
    attended BOOLEAN DEFAULT false,
    delay_minutes INT DEFAULT 0,

    observations TEXT,
    recorded_at TIMESTAMP DEFAULT now()
);
