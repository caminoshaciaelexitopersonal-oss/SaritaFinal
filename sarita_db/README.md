# SARITA DB - Subsistema de Datos Institucional

Este directorio contiene la definición física de la base de datos de SARITA, gobernada como código y estructurada bajo principios de soberanía digital y aislamiento multi-inquilino.

## Estructura de Directorios

- `00_init/`: Extensiones y esquemas base.
- `01_core/`: Modelo base y gestión de Tenants.
- `02_identity/`: Gestión de usuarios, roles y sesiones.
- `03_governance/`: Vía 1 - Estructura institucional y gubernamental.
- `04_agents/`: Definición de agentes autónomos y orquestación IA.
- `05-09 erp_*/`: Vía 2 - Dominios empresariales (Comercial, Operativo, Contable, etc.).
- `10_wallet/`: Sistema transaccional y billeteras.
- `11_delivery/`: Logística y última milla.
- `12_auditoria/`: Trazabilidad forense y logs de sistema.
- `13_ai_memory/`: Memoria semántica y contextos de IA.
- `14_integraciones/`: Pasarelas externas y servicios de terceros.
- `20_relaciones_globales/`: Constraints transversales y llaves foráneas.
- `30_triggers/`: Lógica automática (Auditoría, Hashes de Integridad).
- `40_rls/`: Políticas de Seguridad de Nivel de Fila (RLS) dinámicas.
- `50_indices/`: Optimización de rendimiento.
- `60_migraciones/`: Control de versiones y cambios evolutivos.
- `70_seed/`: Datos maestros iniciales.
- `80_testing/`: Scripts de validación de integridad.

## Reglas de Oro

1. **Una Tabla = Un Archivo**: Cada entidad debe vivir en su propio archivo SQL dentro de su dominio.
2. **Campos Obligatorios**: Todas las tablas deben incluir `id` (UUID), `tenant_id`, `created_at`, `updated_at` y `hash_integridad`.
3. **Aislamiento**: El aislamiento se garantiza automáticamente mediante RLS dinámico aplicado a todos los esquemas de dominio.
4. **Auditoría Automática**: Todas las operaciones son capturadas en `auditoria.system_logs` mediante triggers globales.
5. **Integridad**: No se permiten ediciones manuales. El hash de integridad se recalcula en cada INSERT/UPDATE.

## Despliegue

Para desplegar la base de datos completa en orden jerárquico:

```bash
python sarita_db/deploy.py
```

Requiere la variable de entorno `DATABASE_URL` configurada.

## Convenciones de Nombres

- Esquemas: minúsculas, singular (ej: `identity`, `governance`).
- Tablas: minúsculas, plural (ej: `users`, `entities`).
- Campos: snake_case.
- Llaves Primarias: Siempre `id` tipo UUID.
