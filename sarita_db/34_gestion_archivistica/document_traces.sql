-- Gestión Archivística: Trazabilidad de Documentos
CREATE TABLE core.document_traces (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    document_id UUID NOT NULL, -- FK en 20_global

    accion TEXT NOT NULL, -- visualizado, firmado, compartido, eliminado
    usuario_id UUID NOT NULL, -- FK en 20_global

    timestamp TIMESTAMP DEFAULT now()
);
