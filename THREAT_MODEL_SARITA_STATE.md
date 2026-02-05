# MODELO DE AMENAZAS DE ESTADO (THREAT MODEL SARITA STATE)

**Versión:** 2.0 (Fase Z-DEF)
**Nivel de Exposición:** Nacional / Crítico
**Hipótesis de Conflicto:** No se asume buena fe de ningún actor, interno o externo.

---

## 1. MATRIZ DE AMENAZAS NACIONALES

| Amenaza | Nivel de Riesgo | Descripción | Impacto Potencial |
| :--- | :--- | :--- | :--- |
| **APT (Advanced Persistent Threat)** | **Máximo** | Ataque coordinado por actores estatales o para-estatales extranjeros para infiltrar el Kernel. | Pérdida de soberanía tecnológica y exfiltración masiva de datos institucionales. |
| **Insider con Privilegios** | **Máximo** | Administrador o SuperAdmin que abusa de sus permisos para sabotear el sistema o desviar recursos. | Sabotaje irreversible, alteración de bitácoras (si no hay encadenamiento) y parálisis operativa. |
| **Corrupción Política del Sistema** | **Crítico** | Intentos de la administración de turno para borrar registros históricos o utilizar la IA para proselitismo. | Pérdida de legitimidad institucional y manipulación de la verdad operativa del territorio. |
| **Sabotaje Silencioso** | **Crítico** | Alteración sutil de algoritmos de optimización para causar daño económico acumulativo a largo plazo. | Erosión de la confianza en la IA y desestabilización del tejido empresarial turístico. |
| **Secuestro Institucional** | **Alto** | Tercero (vendedor o partner) que intenta forzar un "Vendor Lock-in" bloqueando actualizaciones críticas. | Dependencia técnica extrema y pérdida de control sobre la evolución del sistema. |
| **Ataque de Cadena de Suministro** | **Alto** | Inyección de código malicioso en librerías de terceros (npm/pip) utilizadas por SARITA. | Compromiso total de las instancias desplegadas sin detección inmediata en el perímetro. |
| **IA Hostil / Prompt Injection** | **Alto** | Manipulación semántica avanzada para engañar a los agentes SARITA y saltar los guardrails del Kernel. | Ejecución de mandatos no autorizados y desinformación en los canales ciudadanos (Vía 3). |

---

## 2. VECTORES DE ATAQUE PRIORITARIOS

1.  **Manipulación de la Bitácora:** Intento de romper la cadena SHA-256 para ocultar acciones ilegítimas.
2.  **Inyección en el Kernel:** Bypass de las `Sovereignty Flags` para forzar la escritura de datos durante el "Modo Ataque".
3.  **Suplantación de Autoridad:** Uso de vulnerabilidades en el middleware JWT para escalar de Turista a SuperAdmin.
4.  **Envenenamiento de Datos:** Inyección de métricas falsas para desviar las propuestas de optimización de la IA.

## 3. POSTURA DE DEFENSA
*   **Aversión al Riesgo:** El sistema preferirá bloquear una operación legítima (falso positivo) antes que permitir una intrusión potencial (falso negativo).
*   **Aislamiento Total:** El ataque debe ser contenido en el nodo afectado; la federación debe actuar como un cortafuegos institucional.

---
**"La mayor amenaza para un Estado no es el ataque que destruye, sino la infiltración que gobierna."**
