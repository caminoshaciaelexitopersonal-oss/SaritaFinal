-- Setup pgvector for AI memory
CREATE EXTENSION IF NOT EXISTS vector;

-- Table for episodic agent memory
CREATE TABLE IF NOT EXISTS ai_core.agent_memory_episodic (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_id UUID NOT NULL,
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    embedding vector(1536), -- Match text-embedding-3 dimensions
    content TEXT,
    relevance_score DECIMAL(5, 4),
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

-- Semantic isolation index
CREATE INDEX ON ai_core.agent_memory_episodic USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);

-- Trigger for memory decay calculation (Conceptual SQL)
-- UPDATE ai_core.agent_memory_episodic SET relevance_score = relevance_score * 0.95 WHERE created_at < NOW() - INTERVAL '30 days';
