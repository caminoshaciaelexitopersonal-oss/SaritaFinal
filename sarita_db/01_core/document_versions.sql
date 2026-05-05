-- Versionado Inmutable
CREATE TABLE archival.document_versions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    document_id UUID NOT NULL, -- FK en 20_global
    version_number INT NOT NULL,

    file_url TEXT NOT NULL,
    binary_hash TEXT NOT NULL, -- SHA256 real del archivo

    author_id UUID NOT NULL, -- FK a users en 20_global

    metadata_snapshot JSONB,
    created_at TIMESTAMP DEFAULT now()
);

-- REGLA: Nunca sobrescribir, solo crear nuevas versiones.
-- Un trigger o RLS debería impedir UPDATES en esta tabla.
CREATE TRIGGER trg_immutable_versions BEFORE UPDATE ON archival.document_versions
FOR EACH ROW EXECUTE FUNCTION core.fn_check_forensic_lock(); -- Reusando lógica de bloqueo
