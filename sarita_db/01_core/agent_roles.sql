CREATE TABLE ai_core.agent_roles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    level INT NOT NULL, -- 1: Asistente, 3: Analista, 6: Soberano
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE OR REPLACE FUNCTION ai_core.fn_validate_agent_level(p_agent_id UUID, p_required_level INT)
RETURNS BOOLEAN AS $$
DECLARE
    v_level INT;
BEGIN
    -- Se asume relación en agents.autonomous_agents o perfil del usuario agente
    SELECT authority_level INTO v_level FROM identity.roles r
    JOIN identity.users u ON u.role = r.name
    WHERE u.id = p_agent_id;

    IF v_level < p_required_level THEN
        RAISE EXCEPTION 'INSUFFICIENT AI LEVEL: Required %, Agent has %', p_required_level, v_level;
    END IF;
    RETURN TRUE;
END;
$$ LANGUAGE plpgsql;
