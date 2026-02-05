# ESPECIFICACIÓN DEL LEGAL KERNEL (LEGAL KERNEL SPEC - LK)

**Versión:** 1.0 (Fase Z-LEGAL)
**Módulo:** `apps.legal_kernel`
**Rol:** Núcleo de Reglas Legales Ejecutables y Gestión Normativa.

---

## 1. NATURALEZA DEL LEGAL KERNEL (LK)
El Legal Kernel es el componente central de SARITA encargado de codificar marcos jurídicos internacionales, tratados y regulaciones locales en lógica técnica procesable. Su función no es interpretar el espíritu de la ley, sino **ejecutar la letra de la norma** mediante condiciones matemáticas y eventos verificables.

## 2. CAPACIDADES CORE

### 2.1 Almacén de Normas Ejecutables
*   **Función:** Actúa como un repositorio centralizado de reglas legales traducidas a código (ej: JSON/DSL).
*   **Contenido:** Cada entrada incluye el identificador legal, la jurisdicción, la vigencia y la lógica de validación técnica asociada.

### 2.2 Versionado Normativo (Normative Versioning)
*   **Función:** Gestiona el ciclo de vida de las leyes.
*   **Capacidad:** Permite la coexistencia de normas (ej: Norma A vigente hasta 2024, Norma B vigente desde 2025). Asegura que los hechos ocurridos en el pasado se evalúen bajo la norma vigente en ese momento.

### 2.3 Gestión de Jurisdicciones por Tratado
*   **Función:** Aplica reglas específicas basadas en el Nodo Nacional o Supranacional de origen.
*   **Lógica:** Una norma de la UE no se ejecuta en un nodo de MERCOSUR a menos que exista un tratado de reciprocidad cargado en el LK.

### 2.4 Sellado de Integridad Legal
*   **Función:** Firma criptográficamente cada regla cargada para asegurar que el motor de cumplimiento no ha sido alterado por actores internos.

## 3. PRINCIPIO DE NO-INTERPRETACIÓN
El LK opera bajo el paradigma de **"Si no es código, no es ley"**.
- Si una ley es ambigua (ej: "usar la IA de manera razonable"), el LK no intenta definir "razonable".
- El LK requiere que el tratado defina parámetros técnicos objetivos (ej: "Latencia < 500ms" o "Registro de logs > 99%").
- Ante la ambigüedad, el LK emite una "Alerta de Zona Gris" y escala el caso a revisión humana (Tribunales).

## 4. INTEGRACIÓN SISTÉMICA
1.  **Input:** El **Compliance Engine (CE)** envía un evento detectado.
2.  **Proceso:** El LK busca la norma aplicable según jurisdicción y tiempo.
3.  **Output:** Retorna un estado de cumplimiento (CUMPLE / NO CUMPLE / AMBIGUO) y solicita el guardado de evidencia en el **Evidence Vault (EV)**.

---
**"El Legal Kernel no es un juez; es el código que asegura que el juez tenga hechos probados sobre los cuales decidir."**
