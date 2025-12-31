# Evidencia de Pruebas Manuales — FASE 10

Este documento contiene la evidencia de las pruebas manuales ejecutadas para validar la observabilidad y el manejo de errores del módulo `gestion_comercial`.

## 1. Prueba de "Camino Feliz" (Creación Exitosa)

Esta prueba verifica que una solicitud válida crea una factura y genera el log de `INFO` esperado.

*   **Acción:** Crear una nueva factura para un perfil con la configuración contable correcta.
*   **Resultado:** Éxito. La factura se creó con un código `201 Created` y el log de `INFO` se registró correctamente.

### Solicitud (Request)
```json
{"cliente_id": "1", "numero_factura": "F-HAPPY-PATH-001", "fecha_emision": "2025-12-29", "items": [{"producto_id": "74b372d0-a994-48b6-a052-748fa7003230", "descripcion": "Prueba de Log", "cantidad": 1, "precio_unitario": 100}]}
```

### Respuesta (Response)
```json
{"id":4,"numero_factura":"F-HAPPY-PATH-001","fecha_emision":"2025-12-29","fecha_vencimiento":null,"subtotal":"100.00","impuestos":"0.00","total":"100.00","total_pagado":"0.00","estado":"BORRADOR","items":[{"id":4,"producto":"74b372d0-a994-48b6-a052-748fa7003230","descripcion":"Prueba de Log","cantidad":"1.00","precio_unitario":"100.00","subtotal":"100.00","impuestos":"0.00"}]}
```

### Log del Backend
```
INFO 2025-12-24 16:03:04,261 views 140081395992384 [FACTURACION] Factura Creada: ID=4, Perfil=a7e5a8e6-2c7c-4c2c-8a3d-4a1b64c8d5e5, Usuario=2
```

---

## 2. Prueba de "Error Controlado" (Configuración Faltante)

*   **Acción Intentada:** Simular un perfil sin cuentas contables para verificar que se devuelve el error contractual estandarizado y se genera un log de `ERROR`.
*   **Resultado:** ❌ **BLOQUEADO**. No se pudo ejecutar la prueba.
*   **Justificación:** Los intentos de crear un perfil de prueba aislado fallaron debido a complejidades en el modelo `Company` (fuera del alcance). Los intentos de eliminar las cuentas contables de un perfil existente fallaron debido a `ProtectedError` de la base de datos, ya que las cuentas ya estaban referenciadas por transacciones creadas en pruebas anteriores.
*   **Verificación de Código:** A pesar del bloqueo de la prueba, se ha verificado manualmente que el código para el manejo de errores contractuales y la observabilidad está correctamente implementado en `presentation/views.py`:
    ```python
    except ChartOfAccount.DoesNotExist:
        logger.error(
            f"[FACTURACION] Error al crear factura: Cuentas contables no encontradas. Perfil={perfil.id}"
        )
        raise serializers.ValidationError({
            "error": "CONFIGURACION_CONTABLE_INCOMPLETA",
            "detalle": "..."
        })
    ```
    Esta implementación cumple con los requisitos de la directriz.
