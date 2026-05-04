CREATE TABLE archival.classification_results (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    document_id UUID NOT NULL,
    rule_id UUID,

    confidence_score DECIMAL(3,2),
    suggested_type_id UUID,

    is_verified BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT now()
);
