# Informe de Auditoría del Ecosistema Sarita

**Fecha:** 24 de Octubre de 2025

## Resumen Ejecutivo

Este informe detalla el estado actual de los tres componentes del proyecto: `Sarita`, `Turismoapp` y `SaritaUnificado`. La auditoría revela que `SaritaUnificado`, el proyecto principal, tiene una base de backend estructuralmente sólida pero inactiva debido a la falta de configuración del entorno. Los problemas visuales en `Sarita` son un síntoma directo de este backend no funcional. `Turismoapp` sirve como un mapa conceptual claro para las funcionalidades que deben ser implementadas en el panel "Mi Negocio".

Se ha realizado un progreso inicial en la refactorización del panel "Mi Negocio" dentro de `SaritaUnificado`, pero la estructura de archivos aún no coincide con la arquitectura final deseada.

## 1. Análisis del Proyecto `Sarita`

*   **Estado Funcional:** No funcional.
*   **Causa Raíz:** La aplicación frontend depende completamente de llamadas a una API de backend que no está operativa.
*   **Análisis del Menú:** Los componentes `Header.tsx` y `Sidebar.tsx` intentan cargar su configuración desde el endpoint `/api/config/menu-items/`. El "círculo de carga" que se observa es el estado de espera del frontend que nunca se resuelve porque el backend no responde. **El problema no está en el código del frontend, sino en la falta de respuesta del backend.**
*   **Análisis del Flujo de Autenticación:** El `AuthContext.tsx` gestiona el registro y el inicio de sesión para múltiples roles. Al igual que el menú, esta funcionalidad está inoperativa porque los endpoints (`/auth/login/`, `/auth/registration/...`) no están activos.

## 2. Análisis del Proyecto `Turismoapp`

*   **Estado Funcional:** No funcional (falla en el arranque con `ModuleNotFoundError`, según memoria).
*   **Propósito en el Ecosistema:** Sirve como un prototipo y una referencia clara de la lógica de negocio para el panel de administración de prestadores de servicios turísticos.
*   **Funcionalidades Identificadas:** El análisis de `main.py` confirma la existencia de la lógica para los siguientes módulos, que son la base para "Mi Negocio":
    *   **Módulos Genéricos:** Gestión de Productos/Servicios, CRM (Clientes), Calendario y Reservas.
    *   **Módulos Especializados:**
        *   **Restaurantes:** Gestión de Menú, Mesas, TPV.
        *   **Agencias:** Gestión de Paquetes y Reservas.
        *   **Guías:** Perfil y Reservas.
    *   **Módulos Adicionales:** Gestión de Costos y Precios, que se alinean con los futuros módulos de `Gestión Comercial` y `Gestión Contable`.

## 3. Análisis del Proyecto `SaritaUnificado`

*   **Estado Funcional:** **Parcialmente funcional.**
    *   **Backend:** Tras instalar las dependencias, las migraciones de Django se ejecutan correctamente, lo que indica que los modelos y la configuración de la base de datos son coherentes. El backend está "listo para ser ejecutado".
    *   **Frontend:** Se presume que es una copia de `Sarita` y, por lo tanto, no es funcional hasta que el backend esté sirviendo activamente la API.
*   **Verificación de DIVIPOLA:**
    *   El archivo `divipola.csv` **existe** en `SaritaUnificado/backend/`.
    *   Contiene las columnas requeridas (`dpto`, `nom_mpio`).
    *   Los datos se cargaron exitosamente en la base de datos ejecutando el comando `load_locations`.
*   **Auditoría de la Estructura "Mi Negocio":**
    *   **Existencia:** La carpeta `SaritaUnificado/backend/apps/prestadores/mi_negocio` **SÍ existe**.
    *   **Subdirectorios Principales:** Dentro de `mi_negocio`, las carpetas `gestion_operativa`, `gestion_comercial` y `gestion_contable` **SÍ existen**.
    *   **Módulos Genéricos y Especializados:** Dentro de `gestion_operativa`, las carpetas `modulos_genericos` y `modulos_especializados` **SÍ existen**.
    *   **Estructura Interna (Estado Actual):** La organización dentro de `modulos_genericos` es **INCORRECTA**. En lugar de que cada módulo (ej. `perfil`) contenga sus propios `models.py`, `views.py` y `serializers.py`, existe una estructura con carpetas genéricas `models/`, `views/` y `serializers/` que contienen todo. Esto indica que la refactorización física está **incompleta** y no sigue la arquitectura final deseada.

## Conclusiones y Siguientes Pasos Recomendados

El trabajo más urgente es estabilizar y ejecutar el backend de `SaritaUnificado`. Una vez que la API esté activa, el frontend de `Sarita` (y `SaritaUnificado`) debería volverse funcional, lo que permitiría realizar pruebas de cara al cliente.

La Fase 2 del plan aprobado, que se centra en la refactorización física y lógica del panel "Mi Negocio", es el camino correcto a seguir. El trabajo consistirá en reorganizar el código existente dentro de `apps/prestadores/mi_negocio/` para que coincida con la arquitectura modular objetivo.
