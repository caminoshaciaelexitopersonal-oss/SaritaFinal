# Informe Técnico de Depuración del Frontend - Proyecto Sarita

**Fecha:** 2025-10-27

**Autor:** Jules

## 1. Objetivo

El objetivo de esta fase era realizar una auditoría completa del sistema Sarita, con un enfoque principal en verificar y corregir el flujo de autenticación y el problema de carga del menú en el frontend de Next.js. El síntoma principal era que la aplicación no se renderizaba, mostrando una pantalla de carga infinita.

## 2. Resumen del Problema

La aplicación frontend no se renderizaba correctamente en un entorno de desarrollo local recién configurado. Las pruebas automatizadas con Playwright fallaban porque la página de inicio de sesión (`/es/login`) nunca mostraba los campos del formulario, quedándose atascada en un estado de carga.

## 3. Proceso de Depuración y Hallazgos

A continuación, se detalla la secuencia de hipótesis investigadas, las acciones tomadas y los resultados observados.

### Hipótesis 1: Base de Datos Vacía (Falta de Datos del Menú)
- **Observación:** La memoria del proyecto indicaba que el menú no se carga si la base de datos está vacía.
- **Acción:** Se ejecutó el comando de gestión `python backend/manage.py setup_menu` para poblar la base de datos con la estructura del menú.
- **Resultado:** **Hipótesis descartada.** El problema de renderizado persistió.

### Hipótesis 2: Configuración Incorrecta de la API
- **Observación:** El frontend podría estar fallando al no poder comunicarse con el backend.
- **Acción:**
    1. Se verificó que los servidores de backend y frontend se estuvieran ejecutando.
    2. Se analizó la configuración de la `baseURL` en `frontend/src/services/api.ts` y las rutas en `backend/puerto_gaitan_turismo/urls.py`.
    3. Se encontró una inconsistencia: el frontend usaba `/api` mientras que algunas rutas del backend estaban bajo `/api/v1/`.
    4. Se unificaron todas las rutas del backend bajo el prefijo `/api/v1/` y se actualizó la `baseURL` en el frontend.
- **Resultado:** **Hipótesis descartada.** El problema de renderizado persistió.

### Hipótesis 3: Caché o Dependencias Corruptas
- **Observación:** Un estado corrupto en la caché de Next.js (`.next`) o en las dependencias (`node_modules`) podría causar errores de renderizado.
- **Acción:** Se detuvieron los servidores, se eliminaron los directorios `frontend/.next` y `frontend/node_modules`, se reinstalaron las dependencias con `npm install` y se reiniciaron los servidores.
- **Resultado:** **Hipótesis descartada.** El problema de renderizado persistió.

### Hipótesis 4: Lógica de Carga Inicial en `EntityContext.tsx`
- **Observación:** Los contextos de React que se ejecutan al inicio pueden bloquear el renderizado si su lógica de obtención de datos falla. Se descubrió que `EntityContext.tsx` intentaba cargar datos de la "entidad" basados en el subdominio, lo cual no existe en un entorno local.
- **Acción:** Se modificó la condición en `EntityContext.tsx` para omitir la llamada a la API no solo en `localhost`, sino también en `127.0.0.1`.
- **Resultado:** **Hipótesis descartada.** El problema de renderizado persistió.

### Hipótesis 5: Lógica de Carga Inicial en `AuthContext.tsx`
- **Observación:** El `useEffect` inicial en `AuthContext.tsx` podría estar manejando incorrectamente el estado de carga (`isLoading`), impidiendo que la aplicación se renderice si la llamada inicial para obtener datos del usuario fallaba o quedaba pendiente.
- **Acción:** Se refactorizó el `useEffect` para asegurar que el estado `isLoading` se estableciera en `false` de manera síncrona, evitando el bloqueo.
- **Resultado:** **Hipótesis descartada.** El problema de renderizado persistió.

### Hipótesis 6: Falta de Variables de Entorno
- **Observación:** El frontend dependía de un valor `fallback` para la URL de la API.
- **Acción:** Se creó un archivo `.env.local` en el directorio `frontend` para definir explícitamente la variable `NEXT_PUBLIC_API_URL`.
- **Resultado:** **Hipótesis descartada.** El problema de renderizado persistió.

### Hipótesis 7: Error de JavaScript en el Cliente
- **Observación:** Un error crítico de JavaScript durante la hidratación podría ser la causa.
- **Acción:** Se modificó el script de Playwright para capturar los logs de la consola del navegador.
- **Resultado:** **Hipótesis descartada.** No se encontraron errores de JavaScript. Los únicos mensajes en la consola eran errores `404 Not Found` para recursos no especificados, lo que sugiere un problema de enrutamiento o de construcción de URLs, pero no un error de ejecución de código.

## 4. Conclusión

A pesar de una investigación exhaustiva y la corrección de múltiples problemas de configuración, estructurales y de lógica de inicialización, la causa raíz del problema de renderizado del frontend no ha podido ser identificada.

El sistema, en su estado actual, no es funcional en el lado del cliente. Se recomienda un análisis más profundo del código del frontend, posiblemente utilizando herramientas de depuración del navegador de forma interactiva, como parte de una futura fase de refactorización total.

## 5. Estado Final del Código

Conforme a las instrucciones, todos los cambios temporales realizados durante esta fase de depuración han sido revertidos para dejar el código base en su estado original y estable.
