# Dashboard de Observabilidad Global y Métricas a Escala

La visibilidad es la base de la estabilidad en un sistema distribuido. SARITA utiliza un panel centralizado para monitorear la salud del ecosistema mundial.

## 1. Métricas de Rendimiento Regional (KPIs)
- **Latencia P99 por Continente:** Tiempo que tarda un usuario en América, Europa o Asia en recibir respuesta.
- **Inter-Region Replication Lag:** Segundos de diferencia entre el Master de DB y sus réplicas mundiales.
- **Agent Drift per Region:** Variación en la coherencia de las decisiones de agentes en diferentes clústeres.

## 2. Visualizaciones Clave

### 2.1 Mapa de Tráfico Global
Mapa de calor que muestra el origen de las solicitudes y la región de AWS que las está procesando.

### 2.2 Estado del Consenso PCA Distribuido
Gráfico de red que muestra si el consenso entre agentes se está logrando localmente o si requiere escalamiento inter-regional debido a inconsistencias de datos.

### 2.3 Monitor de Costos en Tiempo Real
- Costo proyectado mensual por región.
- Identificación de microservicios con sobre-aprovisionamiento (usando métricas de Fase 6).
- Eficiencia del auto-escalado (Pods utilizados vs Pods reservados).

## 3. Alertas de Escalabilidad
- **Threshold Crossing:** Notificación si una región alcanza el 80% de su capacidad reservada.
- **Scale-Up Event:** Registro de cuándo y por qué el sistema añadió más recursos (ej: "Pico de tráfico en temporada de carnavales").
- **Region Isolate:** Alerta roja si una región se desconecta del bus de eventos central.

## 4. Trazabilidad Distribuida (OpenTelemetry)
Cada comando del MCP genera un `Global_Trace_ID`. El dashboard permite seguir este ID a través de:
1. Load Balancer US.
2. Microservicio en US.
3. Llamada a base de datos en US.
4. Consulta de inteligencia a Agente en EU (si aplica).
5. Registro final de Auditoría.

## 5. Reporte Financiero Automático
Generación mensual de un informe ejecutivo que cruza el rendimiento del sistema con el gasto en infraestructura, permitiendo calcular el **Costo por Transacción Exitosa**.
