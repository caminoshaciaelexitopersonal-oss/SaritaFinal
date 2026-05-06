-- sarita_db/80_testing/tenant_isolation_test.sql
-- Validación de aislamiento Multi-Tenant (RLS)

-- 1. Setup session para Tenant A
SET app.current_tenant = '00000000-0000-0000-0000-000000000001';
-- Intentar leer datos de Tenant B (suponiendo que existen)
SELECT * FROM identity.users WHERE tenant_id = '00000000-0000-0000-0000-000000000002';
-- Resultado esperado: 0 filas.

-- 2. Intento de Bypass vía subquery
SELECT count(*) FROM (
    SELECT * FROM tourism.tourist_profiles
    WHERE tenant_id = '00000000-0000-0000-0000-000000000002'
) sub;
-- Resultado esperado: 0.
