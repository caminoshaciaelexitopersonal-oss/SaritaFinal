-- Índices de rendimiento
CREATE INDEX idx_users_email ON identity.users (email);
CREATE INDEX idx_users_tenant ON identity.users (tenant_id);
CREATE INDEX idx_providers_tenant ON erp_operativo.tourism_providers (tenant_id);
CREATE INDEX idx_logs_created_at ON auditoria.system_logs (created_at DESC);
CREATE INDEX idx_logs_record_id ON auditoria.system_logs (record_id);
