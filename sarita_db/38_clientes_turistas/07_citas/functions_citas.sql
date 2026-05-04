-- Función: Reserva de Cita con Lock Transaccional
CREATE OR REPLACE FUNCTION core.fn_reservar_cita(p_slot_id UUID, p_user_id UUID)
RETURNS UUID AS $$
DECLARE
    v_appointment_id UUID;
    v_available BOOLEAN;
BEGIN
    -- 1. Bloqueo transaccional del slot para evitar doble reserva
    SELECT is_available INTO v_available FROM core.appointment_slots WHERE id = p_slot_id FOR UPDATE;

    IF v_available = false THEN
        RAISE EXCEPTION 'Slot no disponible.';
    END IF;

    -- 2. Crear Cita
    INSERT INTO core.appointments (user_id, appointment_type, tenant_id, trace_id)
    VALUES (p_user_id, 'general', '00000000-0000-0000-0000-000000000000', gen_random_uuid())
    RETURNING id INTO v_appointment_id;

    -- 3. Crear Booking
    INSERT INTO core.appointment_bookings (appointment_id, slot_id, tenant_id, trace_id)
    VALUES (v_appointment_id, p_slot_id, '00000000-0000-0000-0000-000000000000', gen_random_uuid());

    -- 4. Marcar slot como no disponible (si capacidad = 1)
    UPDATE core.appointment_slots SET is_available = false WHERE id = p_slot_id;

    RETURN v_appointment_id;
END;
$$ LANGUAGE plpgsql;
