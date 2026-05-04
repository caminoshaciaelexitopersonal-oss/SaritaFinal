CREATE TABLE archival.document_relations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    parent_doc_id UUID NOT NULL,
    child_doc_id UUID NOT NULL,

    relation_type TEXT, -- anexo, respuesta, antecedente

    created_at TIMESTAMP DEFAULT now()
);
