# DISASTER RECOVERY BACKUP SCRIPT (Conceptual)

# 1. Snapshot postgres
# pg_dump -U sarita_root sarita_sovereign > /backups/sql/$(date +%F).sql

# 2. Backup Kafka offsets
# kafka-consumer-groups --bootstrap-server kafka:9092 --all-groups --describe > /backups/kafka/offsets.txt

# 3. Rotate old backups
# find /backups -mtime +30 -delete
