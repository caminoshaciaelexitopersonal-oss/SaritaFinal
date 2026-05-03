-- Control de Concurrencia Global por Recurso (Advisory Locks)
CREATE OR REPLACE FUNCTION core.fn_lock_aggregate(p_aggregate_id UUID)
RETURNS VOID AS $$
BEGIN
    -- Bloqueo transaccional basado en el hash del UUID del recurso
    -- Evita condiciones de carrera en operaciones sobre el mismo agregado
    PERFORM pg_advisory_xact_lock(hashtext(p_aggregate_id::text));
END;
$$ LANGUAGE plpgsql;
