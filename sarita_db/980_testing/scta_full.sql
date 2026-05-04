-- 980_testing/scta_full.sql
-- Test de Integración SCTA (Sistema Cognitivo Transversal de Agentes)

BEGIN;

-- 1. Setup inicial (Tenant y Agente)
INSERT INTO core.tenants (id, name) VALUES ('00000000-0000-0000-0000-000000000001', 'SARITA TEST TENANT');
SET app.current_tenant = '00000000-0000-0000-0000-000000000001';

INSERT INTO ai.agents_master (id, agent_name, hierarchy_level, specialization, domain_scope)
VALUES ('11111111-1111-1111-1111-111111111111', 'SARITA_GUARDIAN', 1, 'GLOBAL_OBSERVER', '{GLOBAL}');

-- 2. Creación de Contexto
INSERT INTO ai.agent_context_universal (id, tenant_id, domain, entity_type, entity_id, trace_id)
VALUES ('22222222-2222-2222-2222-222222222222', '00000000-0000-0000-0000-000000000001', 'TURISMO', 'BOOKING', '33333333-3333-3333-3333-333333333333', gen_random_uuid());

-- 3. Ejecución del Agente
INSERT INTO ai.agent_executions (id, agent_id, context_id, execution_type, tenant_id, trace_id, execution_status)
VALUES ('44444444-4444-4444-4444-444444444444', '11111111-1111-1111-1111-111111111111', '22222222-2222-2222-2222-222222222222', 'REASONING', '00000000-0000-0000-0000-000000000001', gen_random_uuid(), 'COMPLETED');

-- 4. Generación de Memoria (Debe pasar el trigger de ejecución previa)
INSERT INTO ai.agent_memory_global (context_id, agent_id, memory_scope, content, tenant_id)
VALUES ('22222222-2222-2222-2222-222222222222', '11111111-1111-1111-1111-111111111111', 'LONG_TERM', '{"pattern": "High demand in Guatapé"}', '00000000-0000-0000-0000-000000000001');

-- 5. Generación de Decisión
INSERT INTO ai.agent_decisions (agent_id, context_id, decision_type, approved, tenant_id, trace_id)
VALUES ('11111111-1111-1111-1111-111111111111', '22222222-2222-2222-2222-222222222222', 'ADJUST_PRICING', TRUE, '00000000-0000-0000-0000-000000000001', gen_random_uuid());

-- 6. Validar Aislamiento (Debe fallar si insertamos sin tenant_id o trace_id - Validado por triggers)
-- INSERT INTO ai.agent_executions (agent_id, context_id, execution_type) VALUES (...); -- Esto lanzará excepción

ROLLBACK; -- Limpiar para que no afecte la base real si se corre accidentalmente fuera de test
