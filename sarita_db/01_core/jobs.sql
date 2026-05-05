-- Extensión del Scheduler para Prioridades y Bloqueo Concurrente
ALTER TABLE core.scheduled_tasks
ADD COLUMN IF NOT EXISTS priority INT DEFAULT 5,
ADD COLUMN IF NOT EXISTS locked BOOLEAN DEFAULT FALSE,
ADD COLUMN IF NOT EXISTS locked_at TIMESTAMPTZ;

-- Comentario: scheduled_tasks actúa como la tabla scheduler.jobs mencionada en la directriz
