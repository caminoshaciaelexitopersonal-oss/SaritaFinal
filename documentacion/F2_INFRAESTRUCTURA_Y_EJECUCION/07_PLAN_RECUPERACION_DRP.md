# Plan de Recuperación ante Desastres (DRP) - Sistema SARITA

## 1. Objetivos de Recuperación
Se definen métricas estrictas para minimizar el impacto ante fallos catastróficos.

- **RTO (Recovery Time Objective):** < 4 horas (Tiempo máximo para restaurar el servicio).
- **RPO (Recovery Point Objective):** < 15 minutos (Pérdida máxima de datos tolerable).

## 2. Estrategia de Backups

### 2.1 Base de Datos (RDS)
- **Snapshots Diarios:** Retención por 35 días.
- **Point-in-Time Recovery (PITR):** Permite restaurar a cualquier segundo en los últimos 35 días.
- **Copia Multi-Región:** Los snapshots se replican automáticamente a la región secundaria (`us-west-2`).

### 2.2 Almacenamiento de Archivos (S3)
- **Cross-Region Replication (CRR):** Cada archivo subido a la región primaria se replica en tiempo real a la secundaria.
- **Versioning:** Protege contra borrados accidentales o ataques de ransomware.

## 3. Estrategia de Failover (Multi-Región)
El sistema opera en un modelo **Active-Passive** (con infraestructura lista en la región secundaria).

1. **Detección:** El Agente Auditor o el sistema de monitoreo detecta una caída total de la región primaria.
2. **Activación:** Se activan los servicios en la región secundaria (EKS, RDS Replica se promociona a Master).
3. **Redirección:** Route 53 cambia el DNS para apuntar al balanceador de carga de la región secundaria.

## 4. Procedimiento de Recuperación

### 4.1 Fallo de Aplicación (Nivel Pod/Nodo)
- El Orquestador (Kubernetes) reinicia los pods automáticamente.
- El Auto-scaler reemplaza nodos fallidos.

### 4.2 Fallo de Base de Datos
- RDS ejecuta un failover automático a la instancia Standby en otra AZ (Tiempo: < 60 segundos).

### 4.3 Fallo Regional
- Ejecución del plan de failover multi-región detallado en la sección 3.

## 5. Plan de Pruebas y Simulacros
- **Drill Trimestral:** Se realiza un simulacro de recuperación en el entorno de Staging cada 3 meses.
- **Chaos Engineering:** Uso de herramientas (ej. AWS Fault Injection Simulator) para introducir fallos controlados y validar la resiliencia.

## 6. Comunicación de Crisis
- Portal de estado (`status.sarita.com`) externo a la infraestructura principal.
- Canales de notificación automáticos para el equipo técnico y gerencial.
