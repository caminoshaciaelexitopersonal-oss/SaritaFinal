# Pre-Auditoría Técnica - Fase 9

## Checklist de Auditoría

Este documento verifica el estado del sistema con respecto a las directrices de la Fase 9.

| Punto de Control | Estado | Observaciones |
| :--- | :--- | :--- |
| **No hay lógica crítica en frontend** | ✅ **Cumple** | La lógica de negocio crítica, como el flujo de aprobación de publicaciones, ha sido refactorizada a una capa de servicios en el backend. Las vistas son delgadas y llaman a estos servicios. |
| **No hay credenciales en código** | ⚠️ **Cumple (con observaciones)** | La búsqueda de credenciales (`key`, `password`, `secret`) no encontró secretos de producción hardcodeados. Las claves (`SECRET_KEY`, `FIELD_ENCRYPTION_KEY`, etc.) se cargan correctamente desde variables de entorno. Se encontraron contraseñas de prueba (`'password123'`) en archivos de prueba, lo cual es una práctica aceptada. **Observación:** Se encontró una contraseña hardcodeada (`'adminpassword'`) en el comando de `management` `seed_institutional_pages.py`. Aunque no afecta a producción, se recomienda refactorizarlo para que cargue la contraseña desde el entorno. |
| **Variables de entorno separadas** | ✅ **Cumple** | La configuración en `settings.py` demuestra una separación clara. Las variables sensibles (`SECRET_KEY`, `DATABASE_URL`, `SENDGRID_API_KEY`, etc.) se cargan mediante `os.environ.get()`. |
| **Logs activos** | ✅ **Cumple** | La configuración de `LOGGING` se estableció en la Fase 8 para registrar las consultas de la base de datos en modo `DEBUG`, y se mantiene. La configuración por defecto está en nivel `INFO` para `root`. |
| **Manejo de errores centralizado** | ✅ **Cumple** | Django Rest Framework maneja las excepciones de forma centralizada. Las funciones de servicio personalizadas levantan excepciones estándar de DRF (`PermissionDenied`, `ValidationError`), permitiendo que el framework las gestione y devuelva respuestas 4xx consistentes. |
| **API desacoplada del CMS** | ✅ **Cumple** | El sistema no tiene un "CMS" tradicional. La API funciona de manera independiente y sirve datos a un frontend desacoplado (Next.js). Las acciones administrativas se están refactorizando a una capa de servicios, aumentando aún más el desacoplamiento. |
| **Pagos encapsulados** | ❔ **No Aplica** | No hay integración directa con pasarelas de pago en esta fase. La lógica de "Planes y Suscripciones" está en su propia app (`admin_plataforma`), lo que sienta las bases para una futura encapsulación. |
| **Roles bien definidos** | ✅ **Cumple** | El sistema utiliza un `CustomUser` model con un campo `role` explícito. Los permisos se gestionan a través de clases de permisos personalizadas de DRF (`IsAdmin`, `IsAnyAdminOrDirectivo`, etc.) que verifican estos roles. |
| **Rate Limiting (Hardening)** | ✅ **Cumple** | Se ha implementado un `rate limiting` global para usuarios autenticados y anónimos a través de la configuración `DEFAULT_THROTTLE_CLASSES` en `settings.py`. |
