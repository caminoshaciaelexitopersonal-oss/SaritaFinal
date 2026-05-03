-- Índices de rendimiento avanzados - FASE 10

-- Índices compuestos para filtrado rápido por Tenant y Tiempo
CREATE INDEX IF NOT EXISTS idx_events_tenant_time ON events.event_store (tenant_id, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_ledger_tenant_time ON ledger.ledger_entries (tenant_id, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_audit_tenant_time ON auditoria.system_logs (tenant_id, created_at DESC);

-- Índices GIN para búsquedas en campos JSONB
CREATE INDEX IF NOT EXISTS idx_events_payload_gin ON events.event_store USING GIN (payload);
CREATE INDEX IF NOT EXISTS idx_kyc_data_gin ON kyc.kyc_profiles USING GIN (verification_data);
CREATE INDEX IF NOT EXISTS idx_payments_metadata_gin ON payments.payment_intents USING GIN (metadata);

-- Índices parciales para estados activos/pendientes
CREATE INDEX IF NOT EXISTS idx_kyc_pending ON kyc.kyc_profiles (id) WHERE status = 'PENDING';
CREATE INDEX IF NOT EXISTS idx_payments_pending ON payments.payment_intents (id) WHERE status = 'PENDING';
