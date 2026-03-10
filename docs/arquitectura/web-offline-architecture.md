# ARQUITECTURA OFFLINE WEB (PWA) - SARITA v1.0
**Lead Architect:** Jules (Senior AI Software Engineer)
**Date:** March 2026

## 1. Visión General
La plataforma Web de SARITA utiliza **Service Workers** y **Workbox** para garantizar la resiliencia en zonas de baja conectividad.

## 2. Estrategias de Cache (Workbox)
| Tipo de Recurso | Estrategia | Descripción |
| :--- | :--- | :--- |
| **Assets Estáticos** | `CacheFirst` | Carga inmediata desde cache para CSS, JS e imágenes. |
| **Datos de API** | `NetworkFirst` | Intenta red para frescura; fallback a cache si falla. |
| **Dashboards** | `StaleWhileRevalidate` | Carga cache instantáneo y actualiza en background. |

## 3. Cola de Operaciones (Offline Queue)
Cuando no hay conexión, las acciones de escritura del usuario se almacenan en la `offlineQueue` (utilizando LocalStorage/IndexedDB).

### Flujo de Sincronización:
1. El usuario realiza una acción (ej: Crear Reserva).
2. El sistema detecta `navigator.onLine === false`.
3. La acción se encola con un UUID y timestamp.
4. Al detectar evento `online`, el Service Worker dispara el proceso de vaciado de cola.
5. Las acciones se ejecutan secuencialmente contra el backend.

## 4. Indicadores de Estado
La interfaz proporciona feedback en tiempo real sobre el estado de la conexión mediante el componente `ConnectivityIndicator`, evitando la incertidumbre del usuario durante cortes de internet.

---
**Resultado Estratégico:** Esta arquitectura permite que SARITA opere en territorios rurales con la misma confiabilidad que las aplicaciones móviles nativas.
