-- Asegurar consistencia de versiones en el Event Store
-- Nota: La tabla ya tiene aggregate_id y version, agregamos el aggregate_version si fuese distinto
-- o reforzamos el UNIQUE existente.
ALTER TABLE events.event_store
DROP CONSTRAINT IF EXISTS unique_event_version;

ALTER TABLE events.event_store
ADD CONSTRAINT unique_event_version
UNIQUE (aggregate_id, version); -- version actúa como aggregate_version
