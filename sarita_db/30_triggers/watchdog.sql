-- Watchdog de Transacciones Largas
CREATE TABLE core.long_running_transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pid INTEGER,
    duration INTERVAL,
    query TEXT,
    state TEXT,
    tenant_id UUID,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE OR REPLACE FUNCTION core.fn_watchdog_monitor()
RETURNS VOID AS $$
BEGIN
    INSERT INTO core.long_running_transactions (pid, duration, query, state)
    SELECT
        pid,
        now() - xact_start as duration,
        query,
        state
    FROM pg_stat_activity
    WHERE state != 'idle'
    AND (now() - xact_start) > interval '30 seconds';
END;
$$ LANGUAGE plpgsql;
