import axios from 'axios';
import { dbService } from './databaseService';

/**
 * SyncEngine for SARITA Desktop (Fase 3)
 */
class SyncEngine {
  private isOnline: boolean = false;
  private syncInterval: NodeJS.Timeout | null = null;
  private apiUrl: string = '';

  constructor() {
    this.apiUrl = process.env.VITE_API_URL || 'http://localhost:8000/api/v1';
  }

  start() {
    console.log('SyncEngine: Starting...');
    this.syncInterval = setInterval(() => this.processQueue(), 30000); // Try every 30s
  }

  async processQueue() {
    const pendingItems = await dbService.all('SELECT * FROM sync_queue ORDER BY created_at ASC LIMIT 10');
    if (pendingItems.length === 0) return;

    console.log(`SyncEngine: Processing ${pendingItems.length} pending operations...`);

    for (const item of pendingItems) {
      try {
        const payload = JSON.parse(item.payload);
        // Logic to send to backend based on operation_type
        if (item.operation_type === 'CREATE_SALE') {
          await this.sendSale(payload);
        }

        // Mark as synced or delete from queue
        await dbService.run('DELETE FROM sync_queue WHERE id = ?', [item.id]);
        console.log(`SyncEngine: Operation ${item.id} synced successfully.`);
      } catch (error: any) {
        console.error(`SyncEngine: Error syncing item ${item.id}:`, error.message);
        await dbService.run('UPDATE sync_queue SET attempts = attempts + 1, last_error = ? WHERE id = ?',
          [error.message, item.id]);
      }
    }
  }

  private async sendSale(saleData: any) {
    // This would use the Shared SDK or direct axios call
    // await axios.post(`${this.apiUrl}/sales/`, saleData);
    return Promise.resolve(); // Simulated for now
  }

  getStatus() {
    return {
      online: this.isOnline,
      lastSync: new Date().toISOString()
    };
  }
}

export const syncEngine = new SyncEngine();
