CREATE TABLE core.schema_versions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    version VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    executed_at TIMESTAMP DEFAULT now(),
    checksum TEXT NOT NULL,
    executed_by TEXT
);
