-- SQL para habilitar pgvector en el runtime
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS ai_core.agent_episodic_memory (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_id UUID NOT NULL,
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    context_id UUID NOT NULL,
    embedding vector(1536), -- OpenAI Ada-002 / text-embedding-3-small
    content_text TEXT,
    relevance_score DECIMAL(5, 4),
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

CREATE INDEX ON ai_core.agent_episodic_memory USING ivfflat (embedding vector_cosine_ops);
