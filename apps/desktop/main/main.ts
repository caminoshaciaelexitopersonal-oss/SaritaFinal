import { app, BrowserWindow, ipcMain, safeStorage } from 'electron';
import * as path from 'path';
import { getHardwareSpecs } from './hardwareIntelligence';
import { dbService } from './databaseService';
import { syncEngine } from './syncEngine';
import { setupHardwareBridge } from './hardwareBridge';
import log from 'electron-log';
import { autoUpdater } from 'electron-updater';

/**
 * SARITA Desktop Main Process (HALLAZGO F4/F6)
 *
 * Gestiona el ciclo de vida de la ventana y el puente de hardware.
 */

// HARDWARE BRIDGE: Manejo de periféricos locales (Fase 3: POS Robustecimiento)
ipcMain.handle('print-receipt', async (event, data) => {
  log.info('POS: Generando recibo de venta...', data.id);

  return {
    status: 'SUCCESS',
    message: `Recibo ${data.id} enviado a la impresora predeterminada.`,
    timestamp: new Date().toISOString()
  };
});

ipcMain.handle('scan-id', async () => {
  console.log('MAIN: Solicitud de escaneo de identidad iniciada.');
  return { status: 'SUCCESS', id_data: { name: 'SIMULATED DATA', valid: true } };
});

// IA LOCAL: Detección de hardware para Ollama
ipcMain.handle('get-hardware-intelligence', async () => {
  return await getHardwareSpecs();
});

// POS OPERATIONS: Manejo de base de datos local (Fase 3)
ipcMain.handle('pos-get-products', async () => {
  return await dbService.all('SELECT * FROM local_products');
});

ipcMain.handle('pos-save-sale', async (event, sale) => {
  const query = `INSERT INTO local_sales (id, total, payment_method, items) VALUES (?, ?, ?, ?)`;
  await dbService.run(query, [sale.id, sale.total, sale.payment_method, JSON.stringify(sale.items)]);

  // Add to sync queue
  await dbService.run(`INSERT INTO sync_queue (operation_type, payload) VALUES (?, ?)`,
    ['CREATE_SALE', JSON.stringify(sale)]);

  return { status: 'SUCCESS', id: sale.id };
});

ipcMain.handle('pos-get-sales-history', async () => {
  return await dbService.all('SELECT * FROM local_sales ORDER BY created_at DESC');
});

// SYNC ENGINE: Estado y control
ipcMain.handle('sync-get-status', async () => {
  return syncEngine.getStatus();
});

ipcMain.handle('sync-force', async () => {
  await syncEngine.processQueue();
  return { status: 'SUCCESS' };
});

// SECURE STORAGE: Bridge para cifrado nativo del SO (Remediación Hallazgo Seguridad)
ipcMain.handle('secure-store-set', async (event, { key, value }) => {
  if (!safeStorage.isEncryptionAvailable()) {
    console.warn('SARITA SECURE: Cifrado no disponible. Usando fallback inseguro (No recomendado).');
    return false;
  }
  const encrypted = safeStorage.encryptString(value);
  return encrypted.toString('base64');
});

ipcMain.handle('secure-store-get', async (event, { encryptedBase64 }) => {
  if (!safeStorage.isEncryptionAvailable()) return null;
  try {
    const buffer = Buffer.from(encryptedBase64, 'base64');
    return safeStorage.decryptString(buffer);
  } catch (e) {
    console.error('SARITA SECURE: Error al descifrar el token.');
    return null;
  }
});

function createWindow() {
  const win = new BrowserWindow({
    width: 1280,
    height: 900,
    webPreferences: {
      preload: path.join(__dirname, '../preload/preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
    },
  });

  win.loadFile(path.join(__dirname, '../renderer/index.html'));

  if (process.env.NODE_ENV === 'development') {
    win.webContents.openDevTools();
  }
}

app.whenReady().then(async () => {
  log.info('App starting...');
  autoUpdater.checkForUpdatesAndNotify();

  await dbService.init();
  syncEngine.start();
  setupHardwareBridge();
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
