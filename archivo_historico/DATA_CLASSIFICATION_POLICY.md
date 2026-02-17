# POLÍTICA DE CLASIFICACIÓN DE DATOS INTERNACIONALES (DATA CLASSIFICATION POLICY)

**Versión:** 1.0 (Fase Z-INT)
**Estado:** OFICIAL
**Objetivo:** Garantizar que ningún dato sensible o soberano cruce fronteras sin mandato explícito.

---

## 1. NIVELES DE INTERCAMBIO AUTORIZADOS

SARITA clasifica la información internacional en cinco niveles críticos:

| Nivel | Descripción | Ejemplo | Compartible |
| :--- | :--- | :--- | :--- |
| **Nivel 0** | **Metadatos Estadísticos** | Conteo total de turistas, carga de red, número de prestadores. | **✅ SÍ** |
| **Nivel 1** | **Indicadores Agregados** | ROI promedio regional, tendencias de consumo por país, salud del ecosistema. | **✅ SÍ** |
| **Nivel 2** | **Eventos Anonimizados** | Alertas de fraude detectadas, patrones de tráfico sospechosos, reportes de satisfacción sin PII. | **⚠️ BAJO TID** |
| **Nivel 3** | **Datos Operativos** | Facturas detalladas, identidades de prestadores, logs de misiones de agentes. | **❌ NO** |
| **Nivel 4** | **Decisiones Soberanas** | Políticas del Kernel, llaves de cifrado, historial de intervenciones manuales del SuperAdmin. | **❌ NO** |

## 2. REGLAS DE TRÁNSITO DE DATOS
1. **Unidireccionalidad Selectiva:** El Nodo Nacional solo "empuja" (push) los datos autorizados al canal federado; no permite que el nodo extranjero "extraiga" (pull) información a su discreción.
2. **Transformación en el Borde (Edge):** La anonimización y agregación deben ocurrir DENTRO del nodo local antes de ser enviadas al IKERNEL.
3. **Sellado de Propiedad:** Cada paquete de datos enviado lleva un "Sello de Origen" inalterable que identifica al país dueño de la información.

## 3. PROHIBICIONES ABSOLUTAS
Queda terminantemente prohibido el intercambio internacional de:
- Identificaciones personales (Cédulas, Pasaportes, Emails).
- Trazas de ubicación GPS granulares de ciudadanos.
- Secretos comerciales o financieros específicos de los Prestadores de Vía 2.
- Código fuente o parámetros internos del `GovernanceKernel` de cualquier nodo.

## 4. AUDITORÍA DE CLASIFICACIÓN
El IKERNEL realizará una inspección de paquetes (Deep Packet Inspection - DPI) para asegurar que ningún campo marcado como Nivel 3 o 4 esté presente en una comunicación federada, bloqueando el envío y alertando al SuperAdmin local si esto ocurre.

---
**"La confianza internacional nace de la certeza de que lo que es privado sigue siendo privado."**
