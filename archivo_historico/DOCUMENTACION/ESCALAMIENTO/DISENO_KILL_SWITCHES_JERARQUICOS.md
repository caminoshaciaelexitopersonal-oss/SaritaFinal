# DISEÑO DE KILL SWITCHES JERÁRQUICOS
**Control Quirúrgico de la Autonomía IA**

## 1. TIPOLOGÍA DE INTERVENCIÓN
- **Kill Switch Local (Municipio):** Detiene la autonomía IA solo en el territorio municipal. Útil para atender crisis locales (ej: orden público).
- **Kill Switch Regional (Departamento):** Detiene todas las actividades en el nodo departamental y sus municipios asociados.
- **Kill Switch Soberano (Nacional):** Intervención total. El sistema entra en "Modo de Escucha" pasivo en todo el país.

## 2. MECANISMO DE ACTIVACIÓN
1.  **Detección:** El SuperAdmin recibe una alerta de riesgo nivel Rojo.
2.  **Confirmación:** Uso del `CriticalActionDialog` con advertencia de impacto legal.
3.  **Difusión:** La señal de Kill Switch se propaga por el bus de eventos a todos los agentes activos en la jurisdicción afectada.
4.  **Audit Log:** Registro inalterable de quién, cuándo y por qué se activó el bloqueo.

---
**Supremacía Humana en cada centímetro del territorio.**
