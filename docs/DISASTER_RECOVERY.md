# Plan de Recuperación ante Desastres (DRP) - Sarita EOS

## 1. Métricas de Recuperación
- **RTO (Recovery Time Objective):** < 15 minutos.
- **RPO (Recovery Point Objective):** < 1 hora para datos críticos.

## 2. Escenarios de Fallo
### 2.1 Caída de Región Completa
- **Detección:** Global Load Balancer detecta timeout sostenido en la región principal.
- **Acción:** Redirección de tráfico hacia la región secundaria (Passive Hot-Standby).
- **Procedimiento:** Promoción de réplica de lectura en región secundaria a base de datos primaria.

### 2.2 Corrupción de Datos
- **Restauración:** Uso de backups automáticos incrementales.
- **Backup Diario:** Imagen completa a las 00:00 UTC almacenada en Bucket S3 con bloqueo de inmutabilidad (Object Lock).
- **Backup Incremental:** Log de transacciones (WAL) cada 15 minutos.

### 2.3 Fallo Masivo de Software (Bad Deploy)
- **Acción:** Rollback inmediato a la imagen de contenedor estable anterior vía `kubectl rollout undo`.
- **Prevención:** Uso de **Blue-Green Deployment** para validar el 100% de la versión nueva antes de redirigir el tráfico productivo.

## 3. Contactos de Emergencia
- Liderazgo de Infraestructura (SRE)
- Soporte SADI (IA Core)
- Proveedor de Cloud (AWS/Google/Azure)

## 4. Pruebas de Recuperación (Chaos Engineering)
- Se ejecutan simulaciones trimestrales de "Kill Instance" y "Drop Database" en el entorno de Staging para validar que los mecanismos de auto-sanación y failover operan según lo previsto.
