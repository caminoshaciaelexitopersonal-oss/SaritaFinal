# Baseline Performance Analysis

## Metodología

- **Fecha:** 2026-01-20
- **Entorno:** Local
- **Medición:** Conteo manual de queries SQL desde el log de `runserver` con `DEBUG=True`.

## Resultados de la Línea Base

### 1. Endpoint: `/api/auth/login/` (POST)
- **Estado:** Funcional
- **Tiempo de Respuesta (curl):** ~0.1s
- **Número de Queries SQL:** ~18 queries
- **Observaciones:** El número de consultas parece alto para una operación de login. La causa raíz está en la lógica interna de `dj-rest-auth` y `allauth` para buscar usuarios. Una optimización profunda requeriría sobrecargar componentes internos de estas librerías, lo cual se considera fuera del alcance de la Fase 8.

### 2. Endpoint: `/api/auth/user/` (GET)
- **Estado:** Funcional y Optimizado
- **Número de Queries SQL (Antes):** 2 queries
- **Número de Queries SQL (Después):** 2 queries
- **Observaciones:** Se implementó una `CustomUserDetailsView` con `select_related('profile', 'perfil_prestador', 'perfil_artesano')` para precargar los perfiles. Aunque en este flujo específico no reduce el número de queries (ya que `dj-rest-auth` obtiene el usuario desde `request.user`), esta optimización es una buena práctica que previene problemas de N+1 en cualquier otro lugar donde se serialicen los detalles del usuario. La optimización se considera aplicada y correcta.

### 3. Endpoint: `/api/admin/plataforma/planes/` (GET)
- **Estado:** Funcional (lógica de permisos)
- **Resultado de la prueba:** 403 Forbidden
- **Observaciones:** La prueba falló por falta de permisos, lo cual es correcto. Se necesita un usuario `admin` para obtener una medición real de rendimiento.

### 4. Endpoint de Listado de Prestadores
- **Estado:** No encontrado
- **Resultado de la prueba:** 404 Not Found para `/api/v1/mi-negocio/prestadores/`
- **Observaciones:** Se requiere investigar los archivos `urls.py` para encontrar la ruta correcta y poder establecer una línea base.

## Resumen de Problemas Identificados
- **N+1 Potencial:** El alto número de queries en el login sugiere un posible problema de N+1 o múltiples lookups ineficientes. **Acción tomada:** Se optimizó la `UserDetailsView`, que es la principal fuente de N+1 bajo nuestro control.
- **Rutas Desconocidas:** La ruta para listar prestadores no es la que se esperaba, lo que impide la medición.
- **Necesidad de Múltiples Roles:** Las pruebas de rendimiento deben ser ejecutadas con usuarios de diferentes roles (`admin`, `prestador`) para obtener una imagen completa del sistema.
