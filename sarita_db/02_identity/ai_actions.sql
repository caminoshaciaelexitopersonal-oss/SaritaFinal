-- Acciones Ejecutables por la IA (Gobernanza)
CREATE OR REPLACE FUNCTION ai_memory.fn_ai_suspend_user(p_user_id UUID, p_reason TEXT)
RETURNS VOID AS $$
BEGIN
    UPDATE identity.users SET is_active = false WHERE id = p_user_id;
    INSERT INTO auditoria.system_logs (action, table_name, record_id, new_value, tenant_id)
    VALUES ('AI_SUSPENSION', 'identity.users', p_user_id, jsonb_build_object('reason', p_reason), (SELECT tenant_id FROM identity.users WHERE id = p_user_id));
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION ai_memory.fn_ai_freeze_wallet(p_wallet_id UUID, p_reason TEXT)
RETURNS VOID AS $$
BEGIN
    UPDATE wallet.wallets SET status = 'FROZEN' WHERE id = p_wallet_id;
    -- Auditoría omitida para brevedad
END;
$$ LANGUAGE plpgsql;
