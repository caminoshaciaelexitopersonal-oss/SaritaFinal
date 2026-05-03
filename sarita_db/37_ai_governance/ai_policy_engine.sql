CREATE OR REPLACE FUNCTION ai.validate_action(
    p_action TEXT,
    p_actor TEXT
)
RETURNS BOOLEAN AS $$
BEGIN
    -- Regla de Oro: Solo el sistema o agentes autorizados pueden congelar wallets
    IF p_action = 'freeze_wallet' AND p_actor NOT IN ('system', 'governance_agent') THEN
        RETURN FALSE;
    END IF;

    -- Bloqueo preventivo de acciones destructivas
    IF p_action = 'purge_audit_logs' THEN
        RETURN FALSE;
    END IF;

    RETURN TRUE;
END;
$$ LANGUAGE plpgsql;
