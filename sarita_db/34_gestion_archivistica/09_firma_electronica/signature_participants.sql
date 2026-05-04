-- Firma Electrónica: Participantes
CREATE TABLE archival.signature_participants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    request_id UUID NOT NULL,
    user_id UUID NOT NULL,

    signing_order INT DEFAULT 1,
    status TEXT DEFAULT 'pendiente', -- pendiente, firmado, rechazado

    signed_at TIMESTAMP,
    ip_address INET,

    created_at TIMESTAMP DEFAULT now()
);
