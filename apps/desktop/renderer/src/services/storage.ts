import { StorageProvider, tokenManager } from '@sarita/shared-sdk';

/**
 * Proveedor de Almacenamiento Seguro para Desktop (Electron safeStorage)
 * Implementa remediación para el hallazgo de seguridad en la auditoría 2026.
 */
class DesktopStorageProvider implements StorageProvider {
  async getItem(key: string): Promise<string | null> {
    const encrypted = localStorage.getItem(`secure_${key}`);
    if (!encrypted) return null;

    // Desencriptar via IPC usando safeStorage de Electron
    return await (window as any).saritaAPI.secureStore.get(encrypted);
  }

  async setItem(key: string, value: string): Promise<void> {
    // Encriptar via IPC usando safeStorage de Electron
    const encrypted = await (window as any).saritaAPI.secureStore.set(key, value);
    if (encrypted) {
      localStorage.setItem(`secure_${key}`, encrypted);
    }
  }

  async removeItem(key: string): Promise<void> {
    localStorage.removeItem(`secure_${key}`);
  }
}

// Inyectar el proveedor en el SDK para persistencia real en Desktop
tokenManager.setStorage(new DesktopStorageProvider());
