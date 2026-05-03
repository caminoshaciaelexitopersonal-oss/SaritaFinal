CREATE OR REPLACE FUNCTION core.fn_handle_long_transaction()
RETURNS VOID AS $$
BEGIN
    -- Mover transacciones estancadas a la cola de análisis de fallos (DLQ)
    INSERT INTO core.dead_letter_queue (
        original_job_id, job_type, final_payload, error_log, tenant_id
    )
    SELECT
        id,
        'LONG_TRANSACTION_WATCHDOG',
        row_to_json(t)::jsonb,
        'Transacción excedió tiempo máximo permitido: ' || t.duration,
        COALESCE(t.tenant_id, '00000000-0000-0000-0000-000000000000')
    FROM core.long_running_transactions t;

    -- Limpiar tabla de monitoreo
    DELETE FROM core.long_running_transactions;
END;
$$ LANGUAGE plpgsql;
