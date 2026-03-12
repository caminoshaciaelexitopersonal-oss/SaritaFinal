# INVENTARIO DEL SISTEMA EMPRESARIAL (ERP) - FASE F1

## 💎 Núcleo Operativo del Prestador (Vía 2)

### 1. Gestión Comercial
- **Sub-módulos:** Marketing Multicanal, CRM Pipeline, Funnel Builder, AI Studio, Facturación de Ventas.
- **Profundidad:** Alta. Posee lógica de orquestación compleja (aunque bloqueada en FE).
- **Pantallas faltantes:** Configuración de pasarelas de pago reales, analíticas avanzadas de conversión.

### 2. Gestión Contable
- **Sub-módulos:** Asientos Contables, Plan de Cuentas, Libros Auxiliares, Activos Fijos, Compras (Facturas/Proveedores), Inventario Técnico.
- **Profundidad:** Muy Alta. Estructura modular completa para cumplimiento legal.
- **Informes:** Balance General, Estado de Resultados, Libro Mayor, Libro Diario.
- **Pantallas faltantes:** Cierres de periodo automáticos, conciliación fiscal avanzada.

### 3. Gestión Operativa
- **Genéricos:** Perfil Comercial, Catálogo de Productos/Servicios, CRM de Clientes, Reservas, Valoraciones, Galería.
- **Especializados:**
    - **Hoteles:** Gestión de Habitaciones.
    - **Restaurantes:** Menú/Carta, Mesas, TPV Pedidos.
    - **Guías:** Gestión de Rutas.
    - **Transporte:** Flota de Vehículos.
    - **Agencias:** Paquetes Turísticos.
- **Transversales:** SST (Seguridad y Salud en el Trabajo), Gestión de Proyectos.
- **Profundidad:** Alta. Adaptación total al tipo de negocio.

### 4. Gestión Financiera
- **Sub-módulos:** Tesorería, Cuentas Bancarias, Movimientos de Caja, Análisis de Ratios.
- **Profundidad:** Media. Funcionalidad de monitoreo de liquidez completa.
- **Pantallas faltantes:** Integración con bancos vía API (Open Banking), proyecciones de flujo de caja IA.

### 5. Gestión Archivística
- **Sub-módulos:** Expediente Digital, Trazabilidad Documental, Notarización Blockchain (Polygon).
- **Profundidad:** Media. Foco en invariabilidad y cumplimiento legal.
- **Pantallas faltantes:** Firma digital integrada, OCR para lectura de documentos físicos.

---

## 🏛️ Núcleo de Gobernanza (Vía 1)
El SuperAdmin replica la estructura ERP pero a nivel **Sistémico / Transversal**, permitiendo supervisar y auditar los datos agregados de todos los prestadores por dominio.

## 📋 Diagnóstico ERP
El sistema empresarial de Sarita no es un simple CRUD; es una infraestructura ERP completa. La complejidad real reside en la **interconexión de dominios** (ej: una venta comercial genera un asiento contable y descuenta inventario operativo). La Fase F2 debe asegurar que estas costuras funcionen sin fricción visual.
