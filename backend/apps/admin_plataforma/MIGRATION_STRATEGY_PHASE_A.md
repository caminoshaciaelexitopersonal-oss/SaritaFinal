# ESTRATEGIA DE MIGRACIÓN — FASE A: REFRACTOR ESTRUCTURAL

Debido a que este refactor implica cambios profundos en el esquema (Renombramiento de tablas, campos y migración a UUID), se requiere una ejecución controlada de migraciones en el entorno de producción.

## 1. PASOS PREVIOS
1. **Backup Total:** Realizar respaldo de la base de datos actual.
2. **Freeze Window:** Asegurar que no haya operaciones de escritura concurrentes en los módulos afectados.

## 2. EJECUCIÓN DE MIGRACIONES
Debido a las limitaciones del sandbox, las migraciones deben generarse y aplicarse manualmente siguiendo este orden:

### Paso A: Generación
```bash
python manage.py makemigrations admin_payroll admin_fixed_assets admin_procurement admin_inventory admin_budget admin_projects admin_company
```

### Paso B: Validación de SQL
Se recomienda revisar el SQL generado para asegurar que no haya pérdida de datos durante el renombramiento de tablas.
```bash
python manage.py sqlmigrate admin_payroll 0001
```

## 3. MAPEO DE TABLAS (LEGACY -> TARGET)

| Módulo Legacy | Tabla Target | Estándar |
| :--- | :--- | :--- |
| `admin_nomina` | `admin_payroll_*` | UUID + English |
| `admin_activos_fijos`| `admin_fixed_assets_*`| UUID + English |
| `admin_compras` | `admin_procurement_*` | UUID + English |
| `admin_inventario` | `admin_inventory_*` | UUID + English |
| `admin_presupuesto` | `admin_budget_*` | UUID + English |
| `admin_proyectos` | `admin_projects_*` | UUID + English |
| `admin_empresa` | `admin_company_*` | UUID + English |

## 4. INTEGRIDAD SÍSTEMICA
- El **EventBus** es ahora el mediador obligatorio para impactos financieros.
- Se debe verificar que el listener en `admin_contabilidad` esté correctamente registrado en el `ready()` de su `AppConfig`.

---
**Estrategia definida por Jules.**
