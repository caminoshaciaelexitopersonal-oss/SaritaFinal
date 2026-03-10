import { contextBridge, ipcRenderer } from 'electron';

/**
 * SARITA Desktop Preload Script
 *
 * Expone APIs seguras al proceso renderer mediante contextBridge.
 */

contextBridge.exposeInMainWorld('saritaAPI', {
  send: (channel: string, data: any) => {
    const validChannels = ['toMain', 'auth_event'];
    if (validChannels.includes(channel)) {
      ipcRenderer.send(channel, data);
    }
  },
  receive: (channel: string, func: (...args: any[]) => void) => {
    const validChannels = ['fromMain', 'auth_status'];
    if (validChannels.includes(channel)) {
      ipcRenderer.on(channel, (event, ...args) => func(...args));
    }
  },
  getHardwareIntelligence: () => ipcRenderer.invoke('get-hardware-intelligence'),
  secureStore: {
    set: (key: string, value: string) => ipcRenderer.invoke('secure-store-set', { key, value }),
    get: (encryptedBase64: string) => ipcRenderer.invoke('secure-store-get', { encryptedBase64 })
  },
  pos: {
    getProducts: () => ipcRenderer.invoke('pos-get-products'),
    saveSale: (sale: any) => ipcRenderer.invoke('pos-save-sale'),
    getSalesHistory: () => ipcRenderer.invoke('pos-get-sales-history'),
    getInventory: () => ipcRenderer.invoke('pos-get-inventory')
  },
  sync: {
    getStatus: () => ipcRenderer.invoke('sync-get-status'),
    forceSync: () => ipcRenderer.invoke('sync-force')
  },
  hardware: {
    printReceipt: (data: any) => ipcRenderer.invoke('print-receipt', data),
    scanBarcode: (callback: (code: string) => void) => {
      ipcRenderer.on('barcode-scanned', (_event, code) => callback(code));
    }
  }
});
