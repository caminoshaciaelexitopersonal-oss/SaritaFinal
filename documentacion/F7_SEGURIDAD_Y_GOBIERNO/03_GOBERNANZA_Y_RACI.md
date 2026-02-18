# Manual de Gobernanza Global y Modelo RACI - Sistema SARITA

## 1. Comité de Supervisión AI (Comité Virtual de Decisión - CVD)
El CVD es la autoridad suprema del sistema, encargada de resolver conflictos que la IA no puede mediar.

### 1.1 Funciones
- Revisión de decisiones clasificadas como **CRÍTICAS**.
- Ajuste de políticas de gobernanza globales.
- Auditoría trimestral de sesgos en agentes SADI.
- Resolución de escalamientos humanos.

## 2. Modelo RACI de Gobernanza

| Proceso / Actividad | Operador | Agente SADI | Agente Auditor | MCP (Núcleo) | Admin Humano |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Registro de Intención | **R** | **C** | **I** | **A** | **I** |
| Cálculo de Riesgo | **I** | **R** | **C** | **A** | **I** |
| Consenso PCA | **I** | **R** | **C** | **A** | **I** |
| Ejecución Workflow | **I** | **C** | **I** | **A/R** | **I** |
| Ajuste de Pesos | **I** | **C** | **R** | **A** | **I** |
| Aprobación de Política | **I** | **I** | **C** | **R** | **A** |
| Respuesta a Incidentes | **C** | **I** | **R** | **A** | **R** |

* **R (Responsible):** Realiza la tarea.
* **A (Accountable):** Dueño de la tarea, aprueba el resultado final.
* **C (Consulted):** Provee información o criterios.
* **I (Informed):** Se le notifica el resultado.

## 3. Gobierno del Aprendizaje (Evolución)
- **Propuesta:** Generada por el `AdaptiveEngine`.
- **Validación:** El Agente Auditor asegura que no hay conflicto normativo.
- **Autorización:** El Administrador Humano (A) es el único con autoridad para aplicar cambios estructurales en la lógica de decisión o autoridad de agentes.

## 4. Gestión de Responsabilidad Operativa
En caso de fallo sistémico o error de decisión, la trazabilidad SHA-256 permite identificar:
1. El agente que originó la propuesta.
2. El motor que autorizó la ejecución.
3. El administrador que configuró las políticas vigentes en ese momento.
4. El rastro de datos que alimentó la decisión.
