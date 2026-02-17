# MATRIZ DE SABOTAJE Y ESTRÉS OPERATIVO (FASE 3.3)
**Sistema:** SARITA - Gestión Operativa Genérica
**Objetivo:** Forzar fallos para validar resiliencia y contención de daños.

## 1. Escenarios de Sabotaje de Datos (3.1)
| ID | Descripción | Objetivo | Módulo |
|---|---|---|---|
| D-01 | Orden sin contrato_ref_id | Validar rechazo de FK lógica nula. | OrdenOperativa |
| D-02 | Costo con monto negativo | Validar reglas de integridad de negocio. | Costos |
| D-03 | Incidente con estado inexistente | Forzar desbordamiento de Choices. | Incidentes |
| D-04 | Documento con Hash corrupto | Validar integridad archivística. | Documentos |
| D-05 | Duplicidad de UUID en Tarea | Forzar error de Primary Key. | Tareas |

## 2. Escenarios de Sabotaje de Flujo (3.2)
| ID | Descripción | Objetivo | Módulo |
|---|---|---|---|
| F-01 | Completar orden sin tareas | Validar pre-condiciones de cierre. | Flujos |
| F-02 | Registro de costo sin Orden | Probar dependencia de jerarquía. | Costos |
| F-03 | Salto de 'PENDIENTE' a 'COMPLETADA' | Validar transiciones de estado. | OrdenOperativa |
| F-04 | Cancelación durante Ejecución | Validar limpieza de recursos (rollback operativo). | Flujos |

## 3. Escenarios de Sabotaje de Permisos (3.3)
| ID | Descripción | Objetivo | Módulo |
|---|---|---|---|
| P-01 | Turista borrando Orden | Validar aislamiento de inquilinos (Tenants). | API |
| P-02 | Prestador A editando Orden de Prestador B | Validar seguridad de TenantAwareModel. | API |
| P-03 | Usuario sin perfil creando Costo | Validar middleware de perfil obligatorio. | Costos |

## 4. Escenarios de Sabotaje de Concurrencia (3.4)
| ID | Descripción | Objetivo | Módulo |
|---|---|---|---|
| C-01 | Edición simultánea de Orden | Validar bloqueos (Locks) en DB. | OrdenOperativa |
| C-02 | Doble consumo de Inventario | Validar Race Conditions en Stock. | Inventario |

## 5. Escenarios de Sabotaje de Dependencias (3.5)
| ID | Descripción | Objetivo | Módulo |
|---|---|---|---|
| S-01 | Consulta de Estadísticas sin Datos | Validar manejo de ZeroDivision o Nulls. | Estadísticas |
| S-02 | Fallo en Kernel de Gobernanza | Validar modo "Fail-Safe" de Agentes. | Agentes |

## 6. Escenarios de Sabotaje de Persistencia (3.6)
| ID | Descripción | Objetivo | Módulo |
|---|---|---|---|
| R-01 | Interrupción de Transacción | Validar Atomicidad en creación de Orden+Tarea. | DB |
| R-02 | Lectura de registro inconsistente | Validar manejo de excepciones de integridad. | DB |

---
**Nota:** Durante la ejecución, se utilizarán scripts de Python para inyectar estos fallos directamente en la API y la Base de Datos.
