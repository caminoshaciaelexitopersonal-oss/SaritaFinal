CREATE TABLE integrations.webhook_secrets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    provider TEXT NOT NULL,
    secret_hash TEXT NOT NULL,
    version INT NOT NULL,
    created_at TIMESTAMP DEFAULT now(),
    UNIQUE(provider, version)
);
