CREATE OR REPLACE FUNCTION core.fn_lock_scheduled_job(p_job_id UUID)
RETURNS BOOLEAN AS $$
DECLARE
    v_updated_rows INT;
BEGIN
    UPDATE core.scheduled_tasks
    SET locked = TRUE,
        locked_at = now()
    WHERE id = p_job_id
    AND (locked = FALSE OR (now() - locked_at) > interval '1 hour'); -- Autorelease lock después de 1 hora

    GET DIAGNOSTICS v_updated_rows = ROW_COUNT;
    RETURN v_updated_rows > 0;
END;
$$ LANGUAGE plpgsql;
