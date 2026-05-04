-- Catálogo de Eventos de Comportamiento Normalizados
CREATE TABLE core.tourist_event_catalog (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_code TEXT UNIQUE NOT NULL, -- search, click, view, abandon, reserve_attempt, payment_attempt
    description TEXT,
    severity_level INT DEFAULT 1, -- Para analítica/fraude

    created_at TIMESTAMP DEFAULT now()
);

-- Seed básico
INSERT INTO core.tourist_event_catalog (event_code, description) VALUES
('search', 'Búsqueda en el marketplace'),
('click', 'Interacción con elemento'),
('view', 'Visualización de detalle'),
('abandon', 'Abandono de flujo crítico'),
('reserve_attempt', 'Intento de reserva iniciado'),
('payment_attempt', 'Intento de pago en pasarela');
