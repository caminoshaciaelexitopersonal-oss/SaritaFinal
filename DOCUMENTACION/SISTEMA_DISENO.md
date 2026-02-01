# SISTEMA DE DISEÑO ENTERPRISE — SARITA

## 1. Paleta de Color Semántica
El color en Sarita comunica **estado y jerarquía**, no decoración.

### Colores Base (Identidad)
- **Primario (Acción):** `#006D5B` (Teal Metallic). Utilizado para acciones principales (P1) y estados activos.
- **Secundario (Navegación):** `#008B8B`. Utilizado para hover, elementos secundarios y enlaces.
- **Deep (Estructura):** `#1F3438`. Fondo de componentes en modo oscuro y acentos profundos.
- **Black (Absoluto):** `#000000`. Fondo principal en modo noche para maximizar contraste OLED.

### Colores de Estado
- **Éxito (Success):** Emerald-600. Validaciones positivas y misiones completadas.
- **Advertencia (Warning):** Amber-500. Riesgos medios y estados pendientes.
- **Error (Danger):** Red-600. Fallos críticos y bloqueos de Kernel.
- **Informativo (Info):** Indigo-500. Notificaciones de sistema y datos neutros.

---

## 2. Tipografía Funcional
Basada en la fuente **Inter**, optimizada para lectura de datos densos.

| Nivel | Tamaño | Peso | Uso |
| :--- | :--- | :--- | :--- |
| **Título Sistema** | 4xl (36px) | Black (900) | Dashboard principal y cabeceras L0. |
| **Título Módulo** | 2xl (24px) | Bold (700) | Títulos de sección L1/L2. |
| **Subtítulo** | lg (18px) | Medium (500) | Descripciones de cabecera. |
| **Texto Operativo** | base (16px) | Regular (400) | Contenido de tablas y formularios. |
| **Micro-texto** | xs (12px) | Bold (700) | Badges, labels de inputs y metadata. |

---

## 3. Grid y Espaciado
Regla de oro: **Múltiplos de 8px.**

- **Grid Base:** 8px (utilizar `p-2`, `m-4`, `gap-8` de Tailwind).
- **Border Radius:** `0.75rem` (12px) para Cards y Botones principales.
- **Layout:**
    - Sidebar: `w-72` (288px).
    - Contenedor Principal: Max-width escalable según NOC (Network Operations Center).

---

## 4. Modo Día / Noche Nativo
No es una inversión de colores, es un cambio de contexto cognitivo:

- **Modo Día:** Fondo Blanco (`#FFFFFF`), texto Slate-900. Foco en la claridad operativa.
- **Modo Noche:** Fondo Negro (`#000000`), texto Slate-100. Foco en la reducción de fatiga y visibilidad de alertas (Glow effects).

---

## 5. Accesibilidad
- **Contraste:** Mínimo AA (4.5:1) para todo texto operativo.
- **Foco:** Anillo de marca (`ring-brand`) visible en navegación por teclado.
- **Aria:** Atributos `aria-label` descriptivos en todos los botones de acción para compatibilidad con VOZ.
