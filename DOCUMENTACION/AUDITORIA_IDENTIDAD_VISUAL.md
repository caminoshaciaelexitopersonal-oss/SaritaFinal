# AUDITORÍA DE IDENTIDAD VISUAL - FASE F1

## 🎨 Paleta Corporativa Oficial
Se ha verificado la correcta implementación de la paleta institucional en `globals.css`:

| Propiedad | Color Hex | Uso Principal |
| :--- | :--- | :--- |
| **Brand (Teal)** | `#006D5B` | Botones P1, Links activos, Acentos de KPIs. |
| **Brand Light** | `#008B8B` | Hover de botones, Iconografía secundaria. |
| **Brand Deep** | `#1F3438` | Cards en modo oscuro, Fondos de Sidebar. |
| **Corporate Black** | `#000000` | Background principal en modo noche. |

---

## 🌓 Consistencia Modo Día / Noche
El sistema utiliza clases de Tailwind (`dark:`) y variables CSS dinámicas para el cambio de tema.

### ✅ Aciertos Detectados:
1. **Transición Suave:** El uso de variables como `--card` permite que los componentes se adapten automáticamente sin redundancia de clases.
2. **Contraste Legible:** En modo oscuro, el texto `#f8fafc` garantiza legibilidad sobre el fondo `#000000`.
3. **Identidad Preservada:** El color `brand` se mantiene como acento en ambos modos, reforzando la marca.

### ⚠️ Desviaciones Detectadas:
1. **Componentes Legacy:** Algunos componentes en `/components/common/` (ej: `PrestadorCard`) utilizan colores grises (`bg-gray-50`) en lugar de las variables de tema, lo que causa inconsistencias visuales en modo noche.
2. **Sombras:** Las sombras en modo oscuro a veces son demasiado pronunciadas o utilizan colores claros, lo que rompe la estética "Deep" del diseño Enterprise.
3. **Scrollbars:** El custom scrollbar definido en CSS utiliza `bg-brand/20`, lo cual es excelente, pero su visibilidad es baja en fondos muy oscuros.

---

## 📋 Recomendaciones de Diseño
- Migrar todos los colores hardcoded (`gray-100`, `blue-600`) a variables semánticas (`muted`, `primary`).
- Implementar un set de sombras específico para modo noche (`shadow-brand/10`).
- Unificar el radio de borde (border-radius) al estándar de `0.75rem` (12px) definido en el Kernel visual.
