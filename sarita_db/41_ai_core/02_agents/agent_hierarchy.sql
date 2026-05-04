-- 41_ai_core/02_agents/agent_hierarchy.sql
CREATE TABLE ai.agent_hierarchy (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    parent_agent_id UUID REFERENCES ai.agents_master(id),
    child_agent_id UUID REFERENCES ai.agents_master(id),
    level INT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    CONSTRAINT chk_no_self_parent CHECK (parent_agent_id <> child_agent_id)
);

CREATE INDEX idx_ah_parent ON ai.agent_hierarchy(parent_agent_id);
CREATE INDEX idx_ah_child ON ai.agent_hierarchy(child_agent_id);

-- Trigger para prevenir ciclos jerárquicos (básico)
CREATE OR REPLACE FUNCTION ai.fn_check_hierarchy_cycle()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        WITH RECURSIVE hierarchy_path AS (
            SELECT child_agent_id FROM ai.agent_hierarchy WHERE parent_agent_id = NEW.child_agent_id
            UNION ALL
            SELECT ah.child_agent_id FROM ai.agent_hierarchy ah
            JOIN hierarchy_path hp ON ah.parent_agent_id = hp.child_agent_id
        )
        SELECT 1 FROM hierarchy_path WHERE child_agent_id = NEW.parent_agent_id
    ) THEN
        RAISE EXCEPTION 'SARITA SCTA ERROR: Ciclo jerárquico detectado para el agente %', NEW.parent_agent_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_agent_hierarchy_no_cycle
BEFORE INSERT OR UPDATE ON ai.agent_hierarchy
FOR EACH ROW EXECUTE FUNCTION ai.fn_check_hierarchy_cycle();
