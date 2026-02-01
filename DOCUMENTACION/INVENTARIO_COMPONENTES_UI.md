# INVENTARIO DE COMPONENTES UI - FASE F1

## 🧱 Componentes Base (UI Atómico)
Ubicación: `frontend/src/components/ui/`

| Componente | Propósito | Estado |
| :--- | :--- | :--- |
| `Button.tsx` | Botones Enterprise con variantes (brand, outline, ghost). | 🟩 Profesional |
| `Card.tsx` | Contenedores base para KPIs y secciones. | 🟩 Profesional |
| `Input.tsx` / `Textarea.tsx` | Elementos de formulario estándar. | 🟩 Profesional |
| `Table.tsx` | Wrapper para tablas de datos (shcn/ui style). | 🟩 Profesional |
| `Badge.tsx` | Etiquetas de estatus y categorías. | 🟩 Profesional |
| `Dialog.tsx` | Ventanas modales para acciones rápidas. | 🟩 Profesional |

---

## 🏗️ Componentes de Negocio (ERP/Agente)

| Componente | Ubicación | Uso |
| :--- | :--- | :--- |
| `WelcomeDashboard.tsx` | `/components/agent/` | Pantalla de inicio personalizada por rol. |
| `AgentInterface.tsx` | `/components/agent/` | Panel lateral de interacción con SARITA. |
| `FormBuilder.tsx` | `/components/` | Constructor dinámico de formularios (Vía 1). |
| `AtractivosManager.tsx` | `/components/` | CRUD administrativo de sitios turísticos. |
| `MapaInteractivo.tsx` | `/components/common/` | Visualización geográfica de prestadores. |

---

## ⚠️ Hallazgos de Redundancia y Fragmentación
Se han detectado componentes con nombres idénticos o funciones duplicadas en diferentes rutas:

1. **PlaceholderContent:**
   - `frontend/src/components/common/PlaceholderContent.tsx`
   - `frontend/src/components/shared/PlaceholderContent.tsx`
2. **Modales:**
   - `frontend/src/components/Modal.tsx` (Legacy)
   - `frontend/src/components/ui/Modal.tsx` (Nuevo estándar)
3. **Alertas:**
   - `frontend/src/components/common/Alert.tsx`
   - `frontend/src/components/ui/alert.tsx`
4. **Configuración de Sitio:**
   - `frontend/src/components/SiteConfigManager.tsx`
   - `frontend/src/components/admin/SiteConfigManager.tsx`

## 📋 Recomendación de Consolidación
Se requiere unificar la librería de componentes bajo `/components/ui` y mover los componentes de negocio a `/components/features` o similar para evitar confusiones durante la Fase F2.
