-- Particionamiento Físico de Tablas de Alto Volumen
-- Aplicado a: event_store, ledger_entries, system_logs

-- 1. Particionamiento de Auditoría
CREATE TABLE auditoria.system_logs_y2026 PARTITION OF auditoria.system_logs
    FOR VALUES FROM ('2026-01-01') TO ('2027-01-01');

-- 2. Particionamiento de Event Sourcing
CREATE TABLE events.event_store_y2026 PARTITION OF events.event_store
    FOR VALUES FROM ('2026-01-01') TO ('2027-01-01');

-- 3. Particionamiento de Ledger
CREATE TABLE ledger.ledger_entries_y2026 PARTITION OF ledger.ledger_entries
    FOR VALUES FROM ('2026-01-01') TO ('2027-01-01');

COMMENT ON TABLE sarita_db.partition_metadata IS 'Mantenimiento de particiones anuales para escalabilidad World Class.';
