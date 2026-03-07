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
  }
});
