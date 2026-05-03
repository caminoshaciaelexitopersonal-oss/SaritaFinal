-- Lógica de reintentos con Backoff Exponencial
CREATE OR REPLACE FUNCTION retry.calculate_next_retry(attempt INT)
RETURNS TIMESTAMP AS $$
BEGIN
    -- Intervalo: 2^intento minutos (1, 2, 4, 8, 16...)
    RETURN now() + (INTERVAL '1 minute' * POWER(2, attempt));
END;
$$ LANGUAGE plpgsql;
