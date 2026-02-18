# Estrategia de Failover y Tolerancia a Fallas Geográficas

El sistema SARITA está diseñado para sobrevivir a fallos masivos a nivel de región de nube mediante mecanismos automáticos de detección y redirección.

## 1. Detección de Caída Regional
- **Health Checks Globales:** Route 53 monitorea los endpoints del Load Balancer de cada región.
- **Sentinel Agents:** Agentes ligeros del PCA que verifican la conectividad entre regiones.
- **Anomalía de Tráfico:** Si una región deja de reportar métricas de éxito (Fase 6) durante más de 60 segundos, el MCP inicia el protocolo de sospecha de fallo.

## 2. Protocolo de Failover Automático

### Fase 1: Desvío de Tráfico
El DNS inteligente (Route 53) elimina la región fallida del pool de ruteo. El 100% de las nuevas solicitudes se dirigen a las regiones saludables.

### Fase 2: Promoción de Base de Datos
Si la región caída contenía el Master de la base de datos (PostgreSQL), AWS Aurora promociona automáticamente la réplica en la región secundaria a Master en < 1 minuto.

### Fase 3: Re-orquestación de Workflows (WPA)
- El WPA detecta workflows en estado `RUNNING` que estaban anclados a la región caída.
- Se reanudan en la región secundaria recuperando el estado desde la base de datos persistente.
- Los pasos idempotentes se re-ejecutan; los pasos no-idempotentes activan auditoría de estado.

## 3. Tolerancia a Partición de Red
En caso de "Split-Brain" (las regiones no pueden hablar entre sí pero ambas están vivas):
- Se aplica el **Protocolo de Quórum**.
- Solo la región con el Master original o el mayor número de agentes activos mantiene autoridad de escritura.
- Las demás pasan a modo "Solo Lectura" (Read-Only) hasta que se restaure el túnel de interconexión.

## 4. Recuperación Post-Fallo (Failback)
La restauración de la región primaria no implica el retorno inmediato del tráfico.
1. **Sincronización:** Se espera a que los datos acumulados en la región secundaria se repliquen de vuelta.
2. **Smoke Tests:** Se ejecutan pruebas de validación en la región recuperada.
3. **Migración Progresiva:** Se redirige el 10%, 25%, 50% y finalmente el 100% del tráfico original.

## 5. Matriz de Failover por Escenario

| Fallo | Impacto | Recuperación |
| :--- | :--- | :--- |
| **Pérdida de un Nodo** | Mínimo | K8s re-programa pods automáticamente. |
| **Pérdida de una AZ** | Bajo | Load Balancer desvía a AZs saludables. |
| **Caída de Región** | Alto | Redirección DNS global y promoción de DB. |
| **Corrupción de DB** | Crítico | Restauración desde Snapshot inmutable. |
