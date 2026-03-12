# ESTÁNDARES DE ESTADOS UX — SARITA

El sistema prohíbe las pantallas en blanco y los mensajes técnicos crudos. Cada interacción debe tener un estado de retroalimentación definido.

---

## 1. Estado: Cargando (Loading)
**Regla:** Utilizar Skeletons que respeten la geometría final del componente.
- **Tablas:** Skeleton de filas (mínimo 5).
- **Cards:** Skeleton de bloques con gradiente animado.
- **Dashboards:** Carga progresiva de módulos (L0 carga primero).
- **Acciones:** Spinner integrado en botón o overlay traslúcido para envíos de formulario.

---

## 2. Estado: Vacío (Empty State)
**Regla:** Un estado vacío es una oportunidad de conversión o educación.
- **Visual:** Iconografía o ilustración SVG simplificada.
- **Mensaje:** Explicar qué falta (ej: "Aún no tienes rutas turísticas registradas").
- **Acción:** Botón directo para crear el primer registro ("Registrar mi primera ruta").

---

## 3. Estado: Error de Sistema
**Regla:** No mostrar trazas de código.
- **Error 404:** Redirección a Dashboard o Landing con buscador.
- **Error 500:** Pantalla con ilustración, mensaje de "Estamos trabajando en ello" y botón de "Volver al inicio".
- **Error de API:** Toast persistente con opción de "Reintentar".

---

## 4. Estado: Sin Permisos / Bloqueo Kernel
**Regla:** Diferenciar entre "Acceso denegado" e "Intervención soberana".
- **Sin Permisos:** Card central informando que el rol no posee acceso y link para solicitarlo al SuperAdmin.
- **Bloqueo Kernel:** Banner rojo crítico indicando la política activa que restringe la acción (ej: "Auditoría en curso").

---

## 5. Estado: Timeout / Offline
**Regla:** Informar la pérdida de sincronía con el núcleo.
- **Visual:** Topbar cambia a color gris/ámbar con texto "Modo Offline" o "Reconectando...".
- **Comportamiento:** Deshabilitar botones de escritura (POST/PATCH) para evitar inconsistencias en el Kernel.

---

## 📋 Implementación Técnica Sugerida
Se deben crear componentes de orden superior (HOC) o wrappers:
- `<LoadingWrapper isLoading={...}>`
- `<EmptyState icon={...} title={...} action={...} />`
- `<ErrorBoundary />`
