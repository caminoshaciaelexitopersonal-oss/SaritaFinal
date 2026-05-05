-- 20_relaciones/foreign_keys.sql
-- INTEGRIDAD REFERENCIAL CENTRALIZADA - NORMALIZADO

-- [IDENTITY & CORE]
ALTER TABLE identity.users ADD CONSTRAINT fk_user_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [GOVERNANCE]
-- (Asegurar que governance.administrative_acts existe)
-- ALTER TABLE governance.administrative_acts ADD CONSTRAINT fk_act_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);

-- [TOURISM]
-- ALTER TABLE tourism.tourism_providers ADD CONSTRAINT fk_provider_tenant FOREIGN KEY (tenant_id) REFERENCES core.tenants(id);
ALTER TABLE tourism.tourist_profiles ADD CONSTRAINT fk_tourist_user FOREIGN KEY (user_id) REFERENCES identity.users(id);

-- [AI CORE]
ALTER TABLE ai_core.agent_executions ADD CONSTRAINT fk_ae_agent FOREIGN KEY (agent_id) REFERENCES ai_core.agents_master(id);
ALTER TABLE ai_core.agent_executions ADD CONSTRAINT fk_ae_context FOREIGN KEY (context_id) REFERENCES ai_core.agent_context_universal(id);
ALTER TABLE ai_core.agent_memory_global ADD CONSTRAINT fk_am_agent FOREIGN KEY (agent_id) REFERENCES ai_core.agents_master(id);
ALTER TABLE ai_core.agent_memory_global ADD CONSTRAINT fk_am_context FOREIGN KEY (context_id) REFERENCES ai_core.agent_context_universal(id);
