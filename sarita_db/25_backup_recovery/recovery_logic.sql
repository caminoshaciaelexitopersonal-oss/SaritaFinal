-- Estrategia de Backup y Recuperación (PITR)

/*
1. Habilitar WAL Archiving en postgresql.conf:
   archive_mode = on
   archive_command = 'test ! -f /mnt/server/archivedir/%f && cp %p /mnt/server/archivedir/%f'

2. Snapshot diario (Base Backup):
   pg_basebackup -D /backup/data -Ft -z -P

3. Recuperación punto en el tiempo (PITR):
   - Restaurar el último Base Backup.
   - Configurar recovery.conf con:
     restore_command = 'cp /mnt/server/archivedir/%f %p'
     recovery_target_time = '2026-03-15 12:00:00'
*/

CREATE TABLE sarita_db.backup_log (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    backup_type VARCHAR(50), -- FULL, INCREMENTAL, WAL
    status VARCHAR(20),
    storage_path TEXT,
    size_bytes BIGINT,
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ
);
