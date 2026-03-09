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
        'CREATE TABLE IF NOT EXISTS sync_queue (id INTEGER PRIMARY KEY AUTOINCREMENT, endpoint TEXT, method TEXT, payload TEXT, timestamp TEXT)'
      );
    });
  }

  /**
   * Encola una acción para ejecución diferida si no hay red.
   */
  async enqueue(endpoint: string, method: string, payload: any) {
    console.log(`SYNC SARGENTO: Encolando acción para ${endpoint}`);
    return new Promise((resolve, reject) => {
      this.db.transaction(tx => {
        tx.executeSql(
          'INSERT INTO sync_queue (endpoint, method, payload, timestamp) VALUES (?, ?, ?, ?)',
          [endpoint, method, JSON.stringify(payload), new Date().toISOString()],
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
