"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const electron_1 = require("electron");
electron_1.contextBridge.exposeInMainWorld('electronAPI', {
    // Aquí se expondrán funciones seguras para el proceso renderer
    sendMessage: (channel, data) => electron_1.ipcRenderer.send(channel, data),
    onMessage: (channel, func) => {
        electron_1.ipcRenderer.on(channel, (event, ...args) => func(...args));
    },
});
