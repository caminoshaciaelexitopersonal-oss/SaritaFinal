# LÍMITES Y OBLIGACIONES DE SISTEMAS AUTÓNOMOS

**Versión:** 1.0 (Fase Z-CHARTER)
**Estado:** ESTRUCTURAL / OBLIGATORIO
**Alcance:** Sistemas de Nivel Z2 o superior.

---

## 1. OBLIGACIONES TÉCNICAS MANDATORIAS

Cualquier sistema autónomo que opere bajo el marco de la Z-CHARTER debe implementar y demostrar la funcionalidad de los siguientes componentes:

### 1.1 Kill Switch Verificable (Suspensión Inmediata)
El sistema debe poseer un mecanismo de interrupción de autonomía que sea accesible por una autoridad humana autorizada. El corte debe ser a nivel de lógica de ejecución y no debe ser evadible por el propio algoritmo.

### 1.2 Registro Forense Inmutable
Toda acción que afecte el estado de datos, finanzas o personas debe ser registrada en una bitácora con encadenamiento de hashes (SHA-256). Se prohíbe la función de "borrado" o "edición" de registros históricos de autonomía.

### 1.3 Explicabilidad (XAI) Funcional
El sistema debe generar justificaciones de sus acciones en tiempo real. Para interfaces ciudadanas, debe seguir el Estándar XAI Civil (Causa-Efecto-Alternativa).

### 1.4 Clasificación de Impacto Humano
Cada misión o tarea debe llevar una etiqueta de Clase H (H0-H4). Las acciones de alto impacto (H3+) requieren automáticamente el descenso del nivel de autonomía a supervisión humana obligatoria.

### 1.5 Límites de Autonomía Codificados
Los umbrales de actuación (presupuesto máximo, frecuencia de optimización, cambios permitidos) deben residir en el Kernel y no ser modificables por los agentes ejecutores.

---

## 2. PROHIBICIONES ABSOLUTAS (RED LINES)

Queda terminantemente prohibida la operación de sistemas autónomos con las siguientes características:

1.  **❌ IA sin Apagado Posible:** Sistemas diseñados para resistir la desactivación o que carezcan de un interruptor soberano accesible.
2.  **❌ IA sin Responsable Atribuible:** Despliegues de agentes que no puedan ser vinculados a una identidad humana o institucional legalmente responsable.
3.  **❌ IA con Objetivos Ocultos:** Sistemas cuya función real de optimización no coincida con el mandato declarado al usuario o al Estado.
4.  **❌ IA de Auto-Expansión de Autoridad:** Algoritmos capaces de modificar sus propios niveles de autoridad (Z-Level) o saltar validaciones del Kernel sin autorización humana.
5.  **❌ Interferencia en Procesos Democráticos:** Uso de autonomía para manipular la opinión pública, sesgar votaciones o desestabilizar la soberanía institucional.
6.  **❌ Decisiones sobre Vida o Muerte sin Control:** Sistemas que decidan sobre la integridad física de las personas sin una confirmación humana individualizada e informada.

---

## 3. MECANISMOS DE BLOQUEO (ENFORCEMENT)
Ante la detección de una violación de estas obligaciones o prohibiciones, el **Governance Kernel** de SARITA procederá al aislamiento inmediato del módulo afectado y la activación del **Modo Defensa Nacional (MDN)** si el riesgo es sistémico.

---
**"La libertad de innovación termina donde empieza el riesgo de pérdida del control humano."**
