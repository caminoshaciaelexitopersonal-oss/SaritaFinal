-- 40_rls/ai_policies.sql
-- Seguridad de Fila (RLS) para el dominio SCTA (IA)

ALTER TABLE ai.agent_coverage_matrix ENABLE ROW LEVEL SECURITY;
ALTER TABLE ai.agent_context_universal ENABLE ROW LEVEL SECURITY;
ALTER TABLE ai.agent_executions ENABLE ROW LEVEL SECURITY;
ALTER TABLE ai.agent_memory_global ENABLE ROW LEVEL SECURITY;
ALTER TABLE ai.agent_learning ENABLE ROW LEVEL SECURITY;
ALTER TABLE ai.agent_decisions ENABLE ROW LEVEL SECURITY;

-- Política de Aislamiento por Tenant (Mandatorio)
CREATE POLICY ai_coverage_tenant_isolation ON ai.agent_coverage_matrix
    USING (tenant_id = current_setting('app.current_tenant')::UUID);

CREATE POLICY ai_context_tenant_isolation ON ai.agent_context_universal
    USING (tenant_id = current_setting('app.current_tenant')::UUID);

CREATE POLICY ai_execution_tenant_isolation ON ai.agent_executions
    USING (tenant_id = current_setting('app.current_tenant')::UUID);

CREATE POLICY ai_memory_tenant_isolation ON ai.agent_memory_global
    USING (tenant_id = current_setting('app.current_tenant')::UUID);

CREATE POLICY ai_learning_tenant_isolation ON ai.agent_learning
    USING (tenant_id = current_setting('app.current_tenant')::UUID);

CREATE POLICY ai_decision_tenant_isolation ON ai.agent_decisions
    USING (tenant_id = current_setting('app.current_tenant')::UUID);
