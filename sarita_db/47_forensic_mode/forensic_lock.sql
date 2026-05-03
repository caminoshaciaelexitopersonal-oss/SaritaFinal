-- Modo Forense (Congelamiento de Datos)
CREATE OR REPLACE FUNCTION core.fn_activate_forensic_mode()
RETURNS VOID AS $$
BEGIN
    PERFORM set_config('app.forensic_mode', 'true', false);
END;
$$ LANGUAGE plpgsql;

-- Trigger para bloquear escrituras en modo forense
CREATE OR REPLACE FUNCTION core.fn_check_forensic_lock()
RETURNS TRIGGER AS $$
BEGIN
    IF current_setting('app.forensic_mode', true) = 'true' THEN
        RAISE EXCEPTION 'FORENSIC LOCK ACTIVE: Write operations are prohibited during audit investigation.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Integración con triggers globales (Se aplicará en deploy.py)
