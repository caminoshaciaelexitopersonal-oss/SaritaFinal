# ACCESIBILIDAD Y PREPARACIÓN VOICE-FIRST — SARITA

La interfaz de Sarita debe ser operable sin mouse y comprensible para agentes de inteligencia artificial y lectores de pantalla.

---

## 1. Naming Semántico para VOZ (SADI Integration)
Cada elemento interactivo debe poder ser invocado mediante comandos de lenguaje natural.

### Reglas de Nomenclatura:
- **Botones:** `aria-label` debe ser una acción verbal clara (ej: "Crear Factura", "Aprobar Propuesta").
- **Inputs:** `placeholder` semántico y `id` que coincida con el campo de base de datos.
- **Secciones:** Utilizar tags HTML5 (`<nav>`, `<aside>`, `<main>`, `<article>`) para facilitar el escaneo por el motor semántico.

### Mapeo de Comandos:
| Acción Visual | Intención de Voz |
| :--- | :--- |
| Click en Sidebar > Financiero | "Abrir flujo de caja" |
| Click en Tab > Ingresos | "Mostrar ingresos del mes" |
| Click en Botón > Ejecutar | "Ejecutar intervención soberana" |

---

## 2. Accesibilidad Enterprise (AA / AAA)
El sistema cumple con las pautas WCAG 2.1 para entornos corporativos de alta demanda.

### Requerimientos Técnicos:
1. **Contraste de Color:**
    - Texto base: Mínimo 4.5:1.
    - Iconografía crítica: Mínimo 3:1.
2. **Navegación por Teclado:**
    - Todo elemento `clickable` debe ser alcanzable con `TAB`.
    - `Focus Ring` de color `#006D5B` obligatorio.
3. **Escalabilidad:**
    - La UI no debe romperse al aumentar el zoom del navegador al 200%.
    - Uso de unidades relativas (`rem`, `em`) en lugar de `px` para tipografía.

---

## 3. Feedback Visual a Comandos de Voz
Cuando SADI está activo, la UI debe reaccionar visualmente:
- **Estado de Escucha:** Glow sutil alrededor del icono de agente o borde de pantalla en color Teal.
- **Confirmación:** Cambio de color temporal del botón invocado por voz.
- **Error Semántico:** Vibración visual (shake) leve y notificación de "Comando no reconocido".

---

## 4. Lectores de Pantalla (Screen Readers)
- Utilizar `aria-live="polite"` para actualizaciones de KPIs en tiempo real.
- Atributos `aria-expanded` en menús colapsables.
- Tablas con `scope="col"` y `scope="row"` correctamente definidos.
