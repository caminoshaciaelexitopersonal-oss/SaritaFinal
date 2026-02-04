# SST FRONTEND AUDIT - SARITA

**Fecha:** 24 de Mayo de 2024
**Estado:** Plantilla Operativa

## 1. COMPONENTES DEL SG-SST
- **Matriz de Riesgos:** Visualización prioritaria de áreas, procesos y factores de riesgo (Biomecánico, Ergonómico, etc.).
- **Libro de Incidentes:** Registro histórico de eventos (Incidentes, Casi Accidentes) con trazabilidad de estado (Abierto/Cerrado).
- **KPIs de Seguridad:** Monitor de Índice de Accidentalidad y Riesgos Identificados.

## 2. INTERACCIÓN IA (SADI)
- **Alertas de Capacitación:** El sistema incluye una capa de recomendaciones donde SADI sugiere brigadas de emergencia y capacitaciones normativas.
- **Trigger de Programación:** Capacidad visual para agendar sesiones de seguridad recomendadas por la IA.

## 3. CUMPLIMIENTO NORMATIVO
- **Autoevaluación:** Botón funcional para iniciar el diagnóstico de estándares mínimos según la regulación nacional.
- **Reporte Maestro:** Capacidad de generación de evidencia para el Ministerio del Trabajo o autoridades competentes.

## 4. ESTADO DE INTEGRACIÓN
- **Hallazgo:** El módulo SST en el frontend opera actualmente sobre una **Plantilla Operativa Certificada**.
- **Jerarquía de Agentes:** La lógica real reside en la jerarquía de Capitanes de Sarita (`backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/capitanes/gestion_operativa/sg_sst`), quienes están diseñados para auditar y advertir sobre el cumplimiento.
- **Trazabilidad:** Preparado para recibir datos reales de inspecciones y evaluaciones ocupacionales.
