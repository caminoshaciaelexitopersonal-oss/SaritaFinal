# GUÍA DE COMPONENTES ENTERPRISE — FASE F3

Esta guía documenta el uso correcto de los nuevos componentes técnicos implementados para garantizar la consistencia sistémica.

---

## 1. Componentes Core (`src/ui/components/core`)

### 🔘 Button
**Uso:** Acciones e intenciones.
```tsx
<Button variant="primary" size="md" isLoading={false}>
  Guardar Registro
</Button>
```
- **Variantes:** primary, secondary, destructive, outline, ghost.
- **Regla:** Siempre usar `isLoading` para procesos asíncronos en lugar de deshabilitar manualmente.

### 🔘 Input
**Uso:** Captura de datos determinista.
```tsx
<Input label="Email Corporativo" error="Email inválido" placeholder="ejemplo@sarita.ai" />
```

---

## 2. Componentes de Datos (`src/ui/components/data`)

### 🔘 KPICard
**Uso:** Visualización de métricas de decisión.
```tsx
<KPICard
  label="Ingresos Mes"
  value="$12,400"
  trend={{ value: '+12%', type: 'up' }}
  icon={FiDollarSign}
/>
```

### 🔘 DataTable
**Uso:** Gestión de grandes volúmenes de datos.
```tsx
<DataTable
  columns={[{ header: 'Código', accessor: 'code' }, { header: 'Nombre', accessor: (item) => <b>{item.name}</b> }]}
  data={registros}
  isLoading={loading}
/>
```

---

## 3. Estados UX (`src/ui/components/feedback`)

### 🔘 EmptyState
**Uso:** Cuando una consulta devuelve 0 registros. No dejar la pantalla en blanco.
```tsx
<EmptyState
  title="Sin Facturas"
  message="Aún no has emitido facturas este mes."
  onRetry={() => crearFactura()}
  actionLabel="Emitir Primera Factura"
/>
```

---

## 4. Gobernanza Visual (Roles y Temas)

### Cambio de Tema (Día/Noche)
El sistema utiliza variables CSS semánticas. Prohibido usar colores hex o clases de Tailwind específicas de color (`bg-white`, `text-black`) en las vistas. Usar siempre las variables del Design System:
- `bg-[var(--background-main)]`
- `text-[var(--text-primary)]`

### Sidebar Dinámica
La Sidebar se construye automáticamente inyectando el objeto `RoleUIConfig`. No modificar el componente Sidebar para agregar enlaces; hacerlo en `src/ui/role-config/`.
