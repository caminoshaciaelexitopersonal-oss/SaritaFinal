-- Test de segmentación lógica de memoria
SELECT
    entity_type,
    COUNT(*) as records
FROM ai_core.agent_memory_global
GROUP BY entity_type;
