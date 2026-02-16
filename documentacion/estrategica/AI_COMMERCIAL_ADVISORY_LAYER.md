# AI COMMERCIAL ADVISORY LAYER - SARITA

**Fecha:** 24 de Mayo de 2024
**Estado:** Capa Consultiva Operativa

## 1. ESTADO DE LA INTEGRACIÓN SARITA
En la fase F-B, la jerarquía de agentes actúa exclusivamente en modo **Observador y Consultor**, sin autonomía de ejecución directa sobre los datos del prestador.

## 2. COMPONENTES DE ASESORÍA
- **Estudio AI (`LevelAIStudio.tsx`):** Permite la generación de contenido (imágenes, video, texto) bajo demanda del usuario. La IA sugiere hashtags y formatos, pero el usuario debe confirmar la programación.
- **Sugerencia del Capitán Comercial:** Visible en el Pipeline de Oportunidades, recomendando movimientos de leads basados en el tiempo de inactividad.
- **Recomendación IA (Vía 1):** El SuperAdmin visualiza propuestas de optimización de presupuesto de marketing generadas por el motor de detección de patrones.

## 3. DIFERENCIACIÓN DE AUTORIDAD
- **Acción Humana:** Claramente identificada en botones de "Confirmar", "Facturar" y "Programar".
- **Recomendación IA:** Etiquetada como "Sugerencia del Capitán" o "Propuesta de Optimización", requiriendo siempre un trigger manual para su conversión en acción real.

## 4. PRÓXIMOS PASOS (FASE F-F)
- Transición de la Capa de Asesoría a la Capa de Autonomía Condicionada (Nivel 2), permitiendo ejecuciones dentro de umbrales financieros pre-aprobados por el SuperAdmin.
