-- Generador de Hash de Integridad - FASE 10 (Fix Circularity)
CREATE OR REPLACE FUNCTION core.fn_generar_hash_integridad()
RETURNS TRIGGER AS $$
BEGIN
    -- Genera un hash SHA256 de la fila EXCLUYENDO el propio campo hash_integridad
    NEW.hash_integridad := encode(digest((to_jsonb(NEW) - 'hash_integridad')::text, 'sha256'), 'hex');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
