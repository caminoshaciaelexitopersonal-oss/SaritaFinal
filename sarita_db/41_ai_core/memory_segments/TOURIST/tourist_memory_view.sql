CREATE OR REPLACE VIEW ai_core.view_memory_tourist AS
SELECT * FROM ai_core.agent_memory_global WHERE entity_type = 'TOURIST';
