-- Guía de particionamiento para tablas de alto volumen
-- Nota: La creación física de particiones requiere scripts de mantenimiento o triggers automáticos

/*
Tablas particionadas en esta fase:
1. events.event_store (By Range on created_at)
2. ledger.ledger_entries (By Range on created_at)
3. auditoria.system_logs (By Range on created_at)

Ejemplo de creación de partición manual:
CREATE TABLE events.event_store_y2026m03 PARTITION OF events.event_store
    FOR VALUES FROM ('2026-03-01') TO ('2026-04-01');
*/

CREATE TABLE sarita_db.partition_metadata (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    table_name VARCHAR(100) NOT NULL,
    partition_name VARCHAR(100) NOT NULL,
    range_start TIMESTAMPTZ NOT NULL,
    range_end TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);
