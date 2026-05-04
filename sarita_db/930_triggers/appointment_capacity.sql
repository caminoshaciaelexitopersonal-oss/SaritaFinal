-- Escalado Empresarial de Citas (Capacidad y Control)
ALTER TABLE core.appointment_slots
ADD COLUMN capacity INT NOT NULL DEFAULT 1,
ADD COLUMN booked INT DEFAULT 0;

-- Trigger: Validación de Disponibilidad y Capacidad
CREATE OR REPLACE FUNCTION core.fn_validate_appointment_capacity()
RETURNS TRIGGER AS $$
DECLARE
    v_capacity INT;
    v_booked INT;
BEGIN
    -- 🔒 LOCK TRANSACCIONAL SOBRE EL SLOT
    SELECT capacity, booked INTO v_capacity, v_booked
    FROM core.appointment_slots WHERE id = NEW.slot_id FOR UPDATE;

    IF v_booked >= v_capacity THEN
        RAISE EXCEPTION 'Capacidad Agotada: El slot ya no tiene cupos disponibles.';
    END IF;

    -- Incrementar contador
    UPDATE core.appointment_slots SET booked = booked + 1 WHERE id = NEW.slot_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_check_cap ON core.appointment_bookings;
CREATE TRIGGER trg_check_cap BEFORE INSERT ON core.appointment_bookings
FOR EACH ROW EXECUTE FUNCTION core.fn_validate_appointment_capacity();
