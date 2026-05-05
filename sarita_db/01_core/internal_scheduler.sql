-- Scheduler Interno de Tareas Administrativas
CREATE TABLE core.scheduled_tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    task_name VARCHAR(100) UNIQUE NOT NULL,
    frequency_interval INTERVAL NOT NULL,
    last_run_at TIMESTAMPTZ,
    next_run_at TIMESTAMPTZ,
    procedure_name TEXT NOT NULL,
    is_active BOOLEAN DEFAULT true,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

-- Seed de tareas críticas
INSERT INTO core.scheduled_tasks (task_name, frequency_interval, procedure_name, tenant_id) VALUES
('AUTO_RECONCILE', '1 hour', 'reconciliation.fn_auto_reconcile', '00000000-0000-0000-0000-000000000000'),
('KYC_EXPIRY_CHECK', '1 day', 'kyc.fn_auto_invalidate_kyc', '00000000-0000-0000-0000-000000000000');
