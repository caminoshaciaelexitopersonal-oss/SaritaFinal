/**
 * SARITA Service Worker Logic (Workbox)
 * Gestiona el almacenamiento en cache y las estrategias offline.
 */

import { precacheAndRoute } from 'workbox-precaching';
import { registerRoute } from 'workbox-routing';
import { StaleWhileRevalidate, CacheFirst, NetworkFirst } from 'workbox-strategies';
import { CacheableResponsePlugin } from 'workbox-cacheable-response';
import { ExpirationPlugin } from 'workbox-expiration';

// Precache de recursos generados por Next.js
precacheAndRoute((self as any).__WB_MANIFEST || []);

// 1. Estrategia para Imágenes (Cache First)
registerRoute(
  ({ request }) => request.destination === 'image',
  new CacheFirst({
    cacheName: 'sarita-images',
    plugins: [
      new ExpirationPlugin({ maxEntries: 50, maxAgeSeconds: 30 * 24 * 60 * 60 }),
    ],
  })
);

// 2. Estrategia para API y Datos (Network First)
// Prioriza datos frescos, pero permite consulta offline
registerRoute(
  ({ url }) => url.pathname.startsWith('/api/v1/'),
  new NetworkFirst({
    cacheName: 'sarita-api-data',
    plugins: [
      new CacheableResponsePlugin({ statuses: [0, 200] }),
    ],
  })
);

// 3. Estrategia para Dashboards y Layouts (Stale While Revalidate)
// Carga instantánea con actualización en segundo plano
registerRoute(
  ({ url }) => url.pathname.includes('/dashboard'),
  new StaleWhileRevalidate({
    cacheName: 'sarita-dashboards',
  })
);

// 4. Fallback offline
self.addEventListener('fetch', (event: any) => {
  if (event.request.mode === 'navigate') {
    event.respondWith(
      fetch(event.request).catch(() => {
        return caches.match('/offline.html') || Response.error();
      })
    );
  }
});
