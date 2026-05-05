-- 40_rls/policies.sql
ALTER TABLE core.tenants ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON core.tenants USING (id = current_setting('app.current_tenant')::UUID);
-- Aplicar recursivamente en deploy.py o triggers
