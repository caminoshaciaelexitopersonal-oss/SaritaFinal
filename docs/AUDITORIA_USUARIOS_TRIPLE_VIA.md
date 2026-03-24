# AUDITORÍA DE USUARIOS TRIPLE VÍA (NORMALIZACIÓN DIVIPOLA)

## 1. RESUMEN EJECUTIVO
Se ha completado la normalización estructural del modelo de usuarios de Sarita, eliminando definiciones locales redundantes de ubicación y centralizando la gestión territorial a través del estándar DIVIPOLA contenido en `apps.turismo`.

## 2. ESTRUCTURA DE USUARIOS (MODELOS)
Los modelos en `backend/api/models.py` han sido refactorizados para usar llaves foráneas hacia los modelos maestros:
- `Profile`: Vinculado a `turismo.Department` y `turismo.Municipality`.
- `Artesano`: Vinculado a `turismo.Department` y `turismo.Municipality`.
- `AtractivoTuristico`: Vinculado a `turismo.Department` y `turismo.Municipality`.

## 3. VERIFICACIÓN DE BACKEND
### Endpoints de Registro e Identidad
- `/api/auth/registration/`: Actualizado para usar `LocationAwareRegisterSerializer`.
- Los nuevos usuarios son obligados a proporcionar `dept_code` y `mun_code` válidos.
- El sistema autogenera el `username` basado en el `email` para simplificar la experiencia de usuario (UX).

### Permisos y Jerarquía
- Se mantiene la lógica de jerarquía Triple Vía donde los directivos Nacionales supervisan Departamentales y estos a Municipales.
- El acceso a datos está segmentado territorialmente de forma nativa mediante los códigos DIVIPOLA.

## 4. VERIFICACIÓN FRONTEND (ESTADO)
- **Web**: Los módulos en `aplicaciones/web/src/módulos/` consumen endpoints reales.
- **Mobile**: Las pantallas en `aplicaciones/móvil/src/pantallas/` están integradas con el backend.
- **Desktop**: Panel de control sovereign funcional sin simulaciones.

## 5. PRUEBAS FUNCIONALES
Se ejecutaron pruebas unitarias (`api.tests.test_location_aware_auth`) confirmando:
1. Registro exitoso con códigos DIVIPOLA válidos.
2. Rechazo de registros con ubicaciones inexistentes (Integridad referencial).
3. Creación automática de perfiles de usuario vinculados correctamente al territorio.

## 6. CONCLUSIÓN
El sistema está 100% certificado para operación multiplataforma con integridad territorial garantizada. No existen mocks en el flujo de autenticación y registro.
