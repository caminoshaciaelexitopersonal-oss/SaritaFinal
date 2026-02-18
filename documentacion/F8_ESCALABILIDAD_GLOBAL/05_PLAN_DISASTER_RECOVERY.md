# Plan de Recuperación ante Desastres (DRP) - Escala Global

Este documento formaliza los procedimientos para restaurar la integridad del sistema SARITA ante eventos de pérdida total de infraestructura o compromiso masivo de datos.

## 1. Objetivos de Recuperación (Métricas Globales)

| Criticidad | Tipo de Servicio | RTO (Tiempo) | RPO (Dato) |
| :--- | :--- | :--- | :--- |
| **Nivel 1** | Identidad, Núcleo MCP | < 15 minutos | < 1 minuto |
| **Nivel 2** | Finanzas, WPA Activos | < 1 hora | < 5 minutos |
| **Nivel 3** | SADI, Agentes AI | < 4 horas | < 30 minutos |
| **Nivel 4** | Reportes, Analítica | < 24 horas | < 24 horas |

## 2. Estrategia de Copia de Seguridad Inmutable

### 2.1 Snapshots Criptográficos
- Cada 4 horas se genera un snapshot de las bases de datos transaccionales.
- Los snapshots se firman con una llave residente en un HSM (Hardware Security Module) fuera de la cuenta principal de producción.
- **WORM Storage:** Se almacenan en buckets de S3 con políticas de retención que impiden el borrado incluso por el administrador (Object Lock).

### 2.2 Replicación Multi-Nube (Contingencia)
Como seguro de última instancia, se mantiene una copia diaria anonimizada de los datos críticos en un proveedor alternativo (e.g., Google Cloud Storage) para evitar dependencia exclusiva de AWS.

## 3. Protocolos de Restauración Masiva

### 3.1 Procedimiento de Integridad (SHA-256 Validation)
Antes de restaurar un snapshot:
1. El Agente Auditor verifica el hash del snapshot contra el registro del Shadow Ledger.
2. Si los hashes no coinciden, se sospecha de ransomware o corrupción y se utiliza la versión anterior validada.

### 3.2 Despliegue de Infraestructura "Clean Room"
En caso de compromiso de seguridad:
1. Se utiliza **Terraform** para recrear la infraestructura (VPC, clústeres, subredes) en una región completamente nueva.
2. Solo se despliegan artefactos (imágenes Docker) con firma digital verificada.
3. Se inyectan los datos validados del backup.

## 4. Simulacros y Capacitación
- **War Game Semestral:** Se apaga una región completa en el entorno de Staging para validar el failover automático.
- **Chaos Engineering (AWS Fault Injection):** Se inyectan latencias y cortes de red aleatorios en producción para medir la respuesta del sistema.

## 5. Autoridad en el DRP
- El **Comité Virtual de Decisión (CVD)** es el único que puede declarar un "Desastre Global".
- Tras la declaración, el MCP entra en modo `DISASTER_MODE`, priorizando la consistencia sobre la disponibilidad para transacciones financieras.
