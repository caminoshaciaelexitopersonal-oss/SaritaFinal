import * as SQLite from 'expo-sqlite';

/**
 * SARITA Offline Sync Database Service (Fase 9)
 *
 * Este servicio inicializa la base de datos local para operación offline
 * en zonas rurales.
 */

const dbName = 'sarita_offline.db';

export const initDatabase = async () => {
  try {
    const db = await SQLite.openDatabaseAsync(dbName);

    // Crear tablas básicas para caché offline
    await db.execAsync(`
      PRAGMA journal_mode = WAL;
      CREATE TABLE IF NOT EXISTS sync_queue (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_type TEXT NOT NULL,
        payload TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        synced INTEGER DEFAULT 0
      );
      CREATE TABLE IF NOT EXISTS offline_data (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL,
        last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
      );
    `);

    console.log('SARITA: Base de Datos Offline inicializada con éxito.');
    return db;
  } catch (error) {
    console.error('SARITA: Error inicializando la base de datos offline:', error);
    return null;
  }
};
