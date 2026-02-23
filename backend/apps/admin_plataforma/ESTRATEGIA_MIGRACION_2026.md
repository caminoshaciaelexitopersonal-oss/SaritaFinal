# ESTRATEGIA DE MIGRACIÓN SIN RUPTURA - FASE 6 (SARITA 2026)

Para consolidar el núcleo ERP sin detener la operación, se seguirá el siguiente procedimiento de 5 pasos para cada componente identificado.

## 1. PASO 1: EXTRACCIÓN AL CORE
Se crea el modelo o servicio base en `core_erp` siguiendo los nuevos estándares (UUID, English).
- **Ejemplo:** `class BaseBooking(BaseErpModel): ...` en `operational_domain`.

## 2. PASO 2: ADAPTADOR TEMPORAL (SHIM)
En el módulo original (`mi_negocio` o `admin_plataforma`), se redefine la clase antigua para heredar de la nueva o actuar como un proxy.
- **Ejemplo:**
  ```python
  from apps.core_erp.operational_domain.models import BaseBooking
  class Reserva(BaseBooking):
      class Meta:
          proxy = True # O herencia concreta si se mantienen campos legacy
  ```

## 3. PASO 3: REDIRECCIÓN DE IMPORTACIONES
Se actualizan las vistas y sargentos para importar desde `core_erp` o usar el adaptador local, eliminando dependencias laterales.

## 4. PASO 4: VALIDACIÓN Y TESTS
Ejecución del script `validate_architecture.py` y de los tests unitarios para asegurar que la persistencia sigue funcionando correctamente.

## 5. PASO 5: DECOMIISO
Una vez verificado que no existen referencias a la lógica antigua, se elimina el código legacy y se finaliza la migración de datos si fue necesaria.

---
**Procedimiento ratificado por Jules.**
