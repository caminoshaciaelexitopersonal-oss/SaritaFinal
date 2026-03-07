import { initDatabase } from './database';

/**
 * Servicio de Caché Local (SQLite)
 * Fase 02: Almacenamiento de tours recientes y búsquedas.
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
  }
};
