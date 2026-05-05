CREATE TABLE core.expense_policies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    policy_name TEXT NOT NULL,
    rules_definition JSONB NOT NULL, -- {max_amount: X, categories_allowed: []}

    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT now()
);
