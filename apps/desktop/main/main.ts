import { app, BrowserWindow, ipcMain, safeStorage } from 'electron';
import * as path from 'path';
import { getHardwareSpecs } from './hardwareIntelligence';

/**
 * SARITA Desktop Main Process (HALLAZGO F4/F6)
 *
 * Gestiona el ciclo de vida de la ventana y el puente de hardware.
 */

// HARDWARE BRIDGE: Manejo de periféricos locales
ipcMain.handle('print-receipt', async (event, data) => {
  console.log('MAIN: Solicitud de impresión fiscal recibida.', data);
  // Aquí iría la integración real con drivers de impresoras térmicas
  return { status: 'SUCCESS', message: 'Recibo enviado a cola de impresión.' };
});

ipcMain.handle('scan-id', async () => {
  console.log('MAIN: Solicitud de escaneo de identidad iniciada.');
  // Simulación de interacción con escáner USB
  return { status: 'SUCCESS', id_data: { name: 'SIMULATED DATA', valid: true } };
});

// IA LOCAL: Detección de hardware para Ollama
ipcMain.handle('get-hardware-intelligence', async () => {
  return await getHardwareSpecs();
});

// SECURE STORAGE: Bridge para cifrado nativo del SO (Remediación Hallazgo Seguridad)
ipcMain.handle('secure-store-set', async (event, { key, value }) => {
  if (!safeStorage.isEncryptionAvailable()) {
    console.warn('SARITA SECURE: Cifrado no disponible. Usando fallback inseguro (No recomendado).');
    return false;
  }
  const encrypted = safeStorage.encryptString(value);
  // En una implementación real, esto se guardaría en un archivo de configuración local cifrado
  // Para propósitos de este bridge, lo manejaremos via IPC para el renderer
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

  // Carga el renderer unificado
  win.loadFile(path.join(__dirname, '../renderer/index.html'));

  if (process.env.NODE_ENV === 'development') {
    win.webContents.openDevTools();
  }
}

app.whenReady().then(() => {
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
