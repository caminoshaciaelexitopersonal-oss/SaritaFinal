# SARITA ERP - Gestión Operativa (Fase 10.6)

## Arquitectura de Motor Operativo Universal

Este módulo implementa el núcleo funcional de la operación empresarial para todo el ecosistema SARITA, dividiendo la lógica en una base genérica y extensiones sectoriales.

### 32_gestion_operativa (Genérico)
- `01_core`: Unidades operacionales, catálogos extendidos y modalidades.
- `03_ordenes_servicio`: El eje central de ejecución transaccional.
- `05_agenda_programacion`: Motor universal de reservas y time-slots.
- `09_capacidad_ocupacion`: Rastreo de inventario físico (mesas, camas, asientos).
- Otros: Tareas, Recursos, Incidentes, Checklists, Logística y Geo.

### 33_operativa_especializada (Extensiones)
- `01_hoteles`: Habitaciones e inventario.
- `02_restaurantes`: Mesas, Menús y KDS (Kitchen Display System).
- `04_agencias`: Paquetes e itinerarios.
- `08_transporte`: Vehículos y gestión de viajes.

## Reglas Operativas Maestras

1. **Extensión, no Duplicación**: Ninguna tabla sectorial debe recrear lógica de reservas o capacidad; deben vincularse a los módulos genéricos correspondientes.
2. **Orden de Servicio como Núcleo**: Toda acción física (limpieza, cocina, guía, transporte) debe estar respaldada por una `service_order`.
3. **Integración IA**: Los incidentes, órdenes y reservas alimentan automáticamente la memoria de los agentes para optimización proactiva.
4. **Trazabilidad Geo**: El historial de geolocalización permite auditar rutas de transporte y ejecución de guías en tiempo real.
