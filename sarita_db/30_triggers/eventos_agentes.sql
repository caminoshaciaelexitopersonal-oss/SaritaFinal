-- Lógica de eventos disparados por agentes autónomos
CREATE OR REPLACE FUNCTION agents.fn_trigger_agent_event()
RETURNS TRIGGER AS $$
BEGIN
    -- Lógica para notificar al orquestador de cambios realizados por agentes
    IF NEW.is_agent = true THEN
        -- Insertar en una cola de eventos de agentes (pendiente definir tabla)
        NULL;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
