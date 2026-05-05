CREATE TABLE core.ai_sales_actions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    session_id UUID NOT NULL,
    action_type TEXT NOT NULL, -- recommend_product, create_order, apply_discount

    product_id UUID,
    order_id UUID,

    status TEXT DEFAULT 'proposed', -- proposed, executed, rejected

    created_at TIMESTAMP DEFAULT now()
);
