import { api } from './api';

/**
 * SyncEngine - SARITA Desktop
 * Responsable de la sincronización bidireccional entre el almacenamiento local y el cerebro central.
 */
export const SyncEngine = {
  queue: [] as any[],

  /**
   * Registra una operación para sincronización diferida.
   */
  async enqueue(module: string, action: string, payload: any) {
    const operation = {
      id: crypto.randomUUID(),
      module,
      action,
      payload,
      timestamp: new Date().toISOString(),
      status: 'pending'
    };

    this.queue.push(operation);
    console.log(`SyncEngine: Operación encolada [${module}:${action}]`);

    // Intentar sincronizar inmediatamente si hay red
    if (navigator.onLine) {
      await this.processQueue();
    }
  },

  /**
   * Procesa la cola de operaciones pendientes.
   */
  async processQueue() {
    if (this.queue.length === 0) return;

    console.log(`SyncEngine: Procesando ${this.queue.length} operaciones pendientes...`);

    const pending = [...this.queue];
    try {
      const response = await api.post('/sync/batch/', { operations: pending });

      if (response.status === 201 || response.status === 200) {
        // Limpiar solo los procesados exitosamente
        const processedIds = pending.map(o => o.id);
        this.queue = this.queue.filter(o => !processedIds.includes(o.id));
        console.log('SyncEngine: Sincronización exitosa.');
      }
    } catch (err) {
      console.error('SyncEngine: Error en la sincronización. Se reintentará más tarde.', err);
    }
  },

  /**
   * Obtiene el estado de la cola para la UI.
   */
  getStatus() {
    return {
      pendingCount: this.queue.length,
      isOnline: navigator.onLine
    };
  }
};

// Escuchar cambios de red
window.addEventListener('online', () => SyncEngine.processQueue());
