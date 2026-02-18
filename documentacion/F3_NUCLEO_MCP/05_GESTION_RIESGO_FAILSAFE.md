# Gestión de Riesgo y Mecanismos Failsafe (MCP)

## 1. Evaluación de Riesgo en Tiempo Real
El MCP integra un motor de decisión que calcula un **Risk Score (0.0 a 1.0)** para cada comando.

### 1.1 Factores de Cálculo
- **Riesgo Financiero:** Monto de la transacción vs Límites de cuenta.
- **Riesgo Operativo:** Disponibilidad de recursos y carga del sistema.
- **Riesgo Reputacional:** Historial del usuario o prestador.
- **Riesgo de Seguridad:** Origen de la IP, anomalías en el comportamiento previo.

### 1.2 Umbrales de Acción
- **Score < 0.3 (Bajo):** Aprobación automática.
- **0.3 <= Score < 0.7 (Medio):** Requiere validación de un Agente Especialista adicional.
- **Score >= 0.7 (Alto):** Bloqueo automático o requerimiento de aprobación humana (Sovereign).

## 2. Protocolo de Consenso de Agentes
Cuando hay discrepancia entre agentes (ej: Agente de Ventas dice "Sí", Agente de Cumplimiento dice "No"):
1. El MCP prioriza al Agente con mayor **Nivel de Autoridad**.
2. Si el conflicto persiste entre agentes del mismo nivel, se aplica la regla **DENY_BY_DEFAULT** (Denegación por defecto).
3. Se registra el conflicto como un incidente de gobernanza para auditoría humana.

## 3. Mecanismo Failsafe (Seguridad ante Fallos)

### 3.1 Nodo de Respaldo (High Availability)
El MCP corre en un clúster de Kubernetes con múltiples réplicas. Si el nodo líder falla, el mecanismo de elección de líder de K8s activa un secundario que retoma los estados desde la base de datos persistente.

### 3.2 El "Kill-Switch" Global
Existe un comando de emergencia reservado para administradores humanos de alto nivel que puede:
- Congelar toda la orquestación en curso.
- Poner al MCP en modo "Sólo Lectura".
- Forzar un Rollback global si se detecta un compromiso sistémico.

### 3.3 Recuperación Post-Fallo
Al reiniciarse tras un fallo, el MCP escanea la tabla de estados y busca comandos en estado `ORCHESTRATING`. Para cada uno:
1. Verifica si la acción en el PCA se completó.
2. Si está incompleta, decide según la política del comando: `Resume` (Reanudar) o `Compensate` (Rollback).

## 4. Auditoría Inmutable (Shadow Ledger)
Cada evaluación de riesgo se firma digitalmente y se guarda fuera del alcance de los módulos operativos, asegurando que el "por qué" de una decisión nunca pueda ser alterado.
