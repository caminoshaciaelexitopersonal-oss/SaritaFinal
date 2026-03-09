import sqlite3 from 'sqlite3';
import { app } from 'electron';
import * as path from 'path';
import * as fs from 'fs';

/**
 * DatabaseService for SARITA Desktop (Fase 3: Offline First)
 */
class DatabaseService {
  private db: sqlite3.Database | null = null;
  private dbPath: string;

  constructor() {
    const userDataPath = app.getPath('userData');
    this.dbPath = path.join(userDataPath, 'sarita_pos.sqlite');
  }

  async init(): Promise<void> {
    return new Promise((resolve, reject) => {
      this.db = new sqlite3.Database(this.dbPath, (err) => {
        if (err) {
          console.error('Offline DB: Error opening database', err);
          reject(err);
        } else {
          console.log('Offline DB: Database connected at', this.dbPath);
          this.createTables().then(resolve).catch(reject);
        }
      });
    });
  }

  private async createTables(): Promise<void> {
    const queries = [
      `CREATE TABLE IF NOT EXISTS local_products (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock_actual INTEGER DEFAULT 0,
        metadata TEXT
      )`,
      `CREATE TABLE IF NOT EXISTS local_sales (
        id TEXT PRIMARY KEY,
        total REAL NOT NULL,
        payment_method TEXT NOT NULL,
        items TEXT NOT NULL,
        status TEXT DEFAULT 'PENDING',
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        synced_at DATETIME
      )`,
      `CREATE TABLE IF NOT EXISTS sync_queue (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        operation_type TEXT NOT NULL,
        payload TEXT NOT NULL,
        attempts INTEGER DEFAULT 0,
        last_error TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
      )`
    ];

    for (const query of queries) {
      await this.run(query);
    }
  }

  run(query: string, params: any[] = []): Promise<any> {
    return new Promise((resolve, reject) => {
      this.db?.run(query, params, function (err) {
        if (err) reject(err);
        else resolve({ id: this.lastID, changes: this.changes });
      });
    });
  }

  all(query: string, params: any[] = []): Promise<any[]> {
    return new Promise((resolve, reject) => {
      this.db?.all(query, params, (err, rows) => {
        if (err) reject(err);
        else resolve(rows);
      });
    });
  }

  get(query: string, params: any[] = []): Promise<any> {
    return new Promise((resolve, reject) => {
      this.db?.get(query, params, (err, row) => {
        if (err) reject(err);
        else resolve(row);
      });
    });
  }
}

export const dbService = new DatabaseService();
