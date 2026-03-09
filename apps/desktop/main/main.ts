import { app, BrowserWindow, ipcMain } from 'electron';
import * as path from 'path';

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
