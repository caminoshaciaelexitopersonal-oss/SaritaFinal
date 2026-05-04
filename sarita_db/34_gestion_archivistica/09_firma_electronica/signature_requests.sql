-- Firma Electrónica: Solicitudes
CREATE TABLE archival.signature_requests (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    document_version_id UUID NOT NULL, -- Versión específica que se firma
    status TEXT DEFAULT 'pendiente', -- pendiente, en_proceso, completado, expirado

    expires_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT now()
);
