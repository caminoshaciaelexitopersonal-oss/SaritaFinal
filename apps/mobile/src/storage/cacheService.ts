import { initDatabase } from './database';

/**
 * Servicio de Caché Local (SQLite)
 * Fase 02 & 03: Almacenamiento de tours recientes, búsquedas y tickets offline.
 */

export const cacheService = {
  async saveTours(tours: any[]) {
    const db = await initDatabase();
    if (!db) return;

    try {
      await db.runAsync('INSERT OR REPLACE INTO offline_cache (key, value) VALUES (?, ?)', [
        'recent_tours',
        JSON.stringify(tours)
      ]);
    } catch (error) {
      console.error('Error guardando caché de tours:', error);
    }
  },

  async getRecentTours() {
    const db = await initDatabase();
    if (!db) return [];

    try {
      const row: any = await db.getFirstAsync('SELECT value FROM offline_cache WHERE key = ?', ['recent_tours']);
      return row ? JSON.parse(row.value) : [];
    } catch (error) {
      console.error('Error obteniendo caché de tours:', error);
      return [];
    }
  },

  async saveSearch(query: string) {
    const db = await initDatabase();
    if (!db) return;

    try {
      await db.runAsync('INSERT OR REPLACE INTO offline_cache (key, value) VALUES (?, ?)', [
        `search_${query}`,
        new Date().toISOString()
      ]);
    } catch (error) {
      console.error('Error guardando búsqueda en caché:', error);
    }
  },

  async saveTicketOffline(reservationId: string, ticketData: any) {
    const db = await initDatabase();
    if (!db) return;
    try {
      await db.runAsync('INSERT OR REPLACE INTO offline_cache (key, value) VALUES (?, ?)', [
        `ticket_${reservationId}`,
        JSON.stringify(ticketData)
      ]);
    } catch (error) {
      console.error('Error guardando ticket offline:', error);
    }
  },

  async getTicketOffline(reservationId: string) {
    const db = await initDatabase();
    if (!db) return null;
    try {
      const row: any = await db.getFirstAsync('SELECT value FROM offline_cache WHERE key = ?', [`ticket_${reservationId}`]);
      return row ? JSON.parse(row.value) : null;
    } catch (error) {
      return null;
    }
  }
};
