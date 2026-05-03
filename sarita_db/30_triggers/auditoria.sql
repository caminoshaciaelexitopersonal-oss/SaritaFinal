-- Sistema de Auditoría Automática
CREATE OR REPLACE FUNCTION auditoria.fn_audit_trigger()
RETURNS TRIGGER AS $$
DECLARE
    v_old_data JSONB := NULL;
    v_new_data JSONB := NULL;
BEGIN
    IF (TG_OP = 'UPDATE') THEN
        v_old_data := to_jsonb(OLD);
        v_new_data := to_jsonb(NEW);
    ELSIF (TG_OP = 'DELETE') THEN
        v_old_data := to_jsonb(OLD);
    ELSIF (TG_OP = 'INSERT') THEN
        v_new_data := to_jsonb(NEW);
    END IF;

    INSERT INTO auditoria.system_logs (
        user_id, action, table_name, record_id, old_value, new_value, tenant_id
    ) VALUES (
        current_setting('sarita.current_user_id', true)::UUID,
        TG_OP,
        TG_TABLE_SCHEMA || '.' || TG_TABLE_NAME,
        COALESCE(NEW.id, OLD.id),
        v_old_data,
        v_new_data,
        COALESCE(NEW.tenant_id, OLD.tenant_id)
    );

    RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql;

-- Generador de Hash de Integridad
CREATE OR REPLACE FUNCTION core.fn_generar_hash_integridad()
RETURNS TRIGGER AS $$
BEGIN
    -- Genera un hash SHA256 de toda la fila convertida a texto
    NEW.hash_integridad := encode(digest(to_jsonb(NEW)::text, 'sha256'), 'hex');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
