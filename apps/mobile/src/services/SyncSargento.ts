import * as SQLite from 'expo-sqlite';
import { api } from './api';

/**
 * SYNC SARGENTO (N5) - MOBILE APP (HALLAZGO F5/F6)
 * Responsable de la sincronización resiliente Offline -> Online.
 */

interface SyncItem {
  id: number;
  endpoint: string;
  method: string;
  payload: string;
  timestamp: string;
}

class SyncSargento {
  private db: SQLite.WebSQLDatabase;

  constructor() {
    this.db = SQLite.openDatabase('sarita_sync.db');
    this.initDatabase();
  }

  private initDatabase() {
    this.db.transaction(tx => {
      tx.executeSql(
        'CREATE TABLE IF NOT EXISTS sync_queue (id INTEGER PRIMARY KEY AUTOINCREMENT, endpoint TEXT, method TEXT, payload TEXT, timestamp TEXT, local_audit TEXT)'
      );
      // Fase 4: Tabla de Caché para optimización de UX
      tx.executeSql(
        'CREATE TABLE IF NOT EXISTS local_cache (key TEXT PRIMARY KEY, value TEXT, expires_at DATETIME)'
      );
    });
  }

  async setCache(key: string, value: any, ttlMinutes: number = 60) {
    const expiresAt = new Date(Date.now() + ttlMinutes * 60000).toISOString();
    return new Promise((resolve) => {
      this.db.transaction(tx => {
        tx.executeSql(
          'INSERT OR REPLACE INTO local_cache (key, value, expires_at) VALUES (?, ?, ?)',
          [key, JSON.stringify(value), expiresAt],
          () => resolve(true)
        );
      });
    });
  }

  async getCache(key: string) {
    return new Promise((resolve) => {
      this.db.transaction(tx => {
        tx.executeSql(
          'SELECT value FROM local_cache WHERE key = ? AND expires_at > ?',
          [key, new Date().toISOString()],
          (_, { rows }) => {
            if (rows.length > 0) {
              resolve(JSON.parse((rows as any)._array[0].value));
            } else {
              resolve(null);
            }
          }
        );
      });
    });
  }

  /**
   * Encola una acción para ejecución diferida si no hay red.
   * Soporta órdenes procesadas por IA local.
   */
  async enqueue(endpoint: string, method: string, payload: any, processedLocally: boolean = false) {
    console.log(`SYNC SARGENTO: Encolando acción para ${endpoint}`);
    return new Promise((resolve, reject) => {
      this.db.transaction(tx => {
        tx.executeSql(
          'INSERT INTO sync_queue (endpoint, method, payload, timestamp, local_audit) VALUES (?, ?, ?, ?, ?)',
          [
            endpoint,
            method,
            JSON.stringify(payload),
            new Date().toISOString(),
            processedLocally ? 'LOCAL_IA_PROCESSED' : 'USER_ACTION'
          ],
          (_, result) => resolve(result),
          (_, error) => { reject(error); return false; }
        );
      });
    });
  }

  /**
   * Vacía la cola de sincronización hacia el backend real.
   */
  async flush() {
    console.log('SYNC SARGENTO: Iniciando vaciado de cola (Flush)...');

    return new Promise((resolve, reject) => {
      this.db.transaction(tx => {
        tx.executeSql('SELECT * FROM sync_queue ORDER BY timestamp ASC', [], async (_, { rows }) => {
          const items = (rows as any)._array as SyncItem[];

          for (const item of items) {
            try {
              console.log(`SYNC SARGENTO: Procesando ${item.endpoint}...`);
              await api.request({
                url: item.endpoint,
                method: item.method,
                data: JSON.parse(item.payload)
              });

              // Eliminar de la cola tras éxito
              this.removeItem(item.id);
            } catch (error) {
              console.error(`SYNC SARGENTO: Error sincronizando ${item.id}. Reintento en próximo ciclo.`, error);
              break; // Detener flush ante error de red
            }
          }
          resolve(true);
        });
      });
    });
  }

  private removeItem(id: number) {
    this.db.transaction(tx => {
      tx.executeSql('DELETE FROM sync_queue WHERE id = ?', [id]);
    });
  }
}

export const syncSargento = new SyncSargento();
