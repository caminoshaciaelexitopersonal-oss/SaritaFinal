CREATE OR REPLACE FUNCTION ai.execute_action(
    p_action TEXT,
    p_payload JSONB
)
RETURNS VOID AS $$
DECLARE
    v_actor TEXT := current_setting('sarita.ai_actor', true);
BEGIN
    IF NOT ai.validate_action(p_action, COALESCE(v_actor, 'anonymous')) THEN
        RAISE EXCEPTION 'Unauthorized AI action: % attempted by %', p_action, v_actor;
    END IF;

    -- Lógica de despacho de acciones
    IF p_action = 'freeze_wallet' THEN
        PERFORM ai_memory.fn_ai_freeze_wallet((p_payload->>'wallet_id')::UUID, p_payload->>'reason');
    ELSIF p_action = 'suspend_user' THEN
        PERFORM ai_memory.fn_ai_suspend_user((p_payload->>'user_id')::UUID, p_payload->>'reason');
    END IF;
END;
$$ LANGUAGE plpgsql;
