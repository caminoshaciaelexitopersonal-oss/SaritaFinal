/**
 * PHASE 2: Mobile Offline Resilience
 * Implements an immutable transaction queue for offline-first operations.
 */
import * as SQLite from 'expo-sqlite';
import * as Crypto from 'expo-crypto';
import { SyncService } from '@sarita/shared-sdk';

const db = SQLite.openDatabaseSync('sarita_offline.db');

export interface OfflineTransaction {
  transaction_id: string;
  user_id: string;
  device_id: string;
  timestamp: string;
  payload: any;
  hash: string;
  previous_hash: string;
  status: 'PENDING' | 'SYNCED' | 'FAILED';
}

export class SyncSargento {
  static async init() {
    await db.execAsync(`
      CREATE TABLE IF NOT EXISTS offline_transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        transaction_id TEXT UNIQUE,
        user_id TEXT,
        device_id TEXT,
        timestamp TEXT,
        payload TEXT,
        hash TEXT,
        previous_hash TEXT,
        status TEXT DEFAULT 'PENDING'
      );
    `);
  }

  static async recordTransaction(payload: any, userId: string, deviceId: string) {
    const timestamp = new Date().toISOString();
    const transaction_id = Crypto.randomUUID();

    // Get last hash for chaining
    const lastTx = await db.getFirstAsync<OfflineTransaction>(
      'SELECT hash FROM offline_transactions ORDER BY id DESC LIMIT 1'
    );
    const previous_hash = lastTx ? lastTx.hash : 'GENESIS';

    // Create current hash (SHA-256)
    const content = `${transaction_id}${timestamp}${JSON.stringify(payload)}${previous_hash}`;
    const hash = await Crypto.digestStringAsync(Crypto.CryptoDigestAlgorithm.SHA256, content);

    await db.runAsync(
      'INSERT INTO offline_transactions (transaction_id, user_id, device_id, timestamp, payload, hash, previous_hash) VALUES (?, ?, ?, ?, ?, ?, ?)',
      [transaction_id, userId, deviceId, timestamp, JSON.stringify(payload), hash, previous_hash]
    );

    return transaction_id;
  }

  static async syncQueue() {
    const pending = await db.getAllAsync<OfflineTransaction>(
      "SELECT * FROM offline_transactions WHERE status = 'PENDING' ORDER BY id ASC"
    );

    for (const tx of pending) {
      try {
        await SyncService.syncLocalChanges(tx);
        await db.runAsync(
          "UPDATE offline_transactions SET status = 'SYNCED' WHERE transaction_id = ?",
          [tx.transaction_id]
        );
      } catch (err) {
        console.error(`Sync failed for ${tx.transaction_id}`, err);
      }
    }
  }
}
