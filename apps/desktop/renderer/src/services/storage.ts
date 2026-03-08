import { StorageProvider, tokenManager } from '@sarita/shared-sdk';

/**
 * Proveedor de Almacenamiento para Desktop (LocalStorage)
 */
class DesktopStorageProvider implements StorageProvider {
  async getItem(key: string): Promise<string | null> {
    return localStorage.getItem(key);
  }
  async setItem(key: string, value: string): Promise<void> {
    localStorage.setItem(key, value);
  }
  async removeItem(key: string): Promise<void> {
    localStorage.removeItem(key);
  }
}

// Inyectar el proveedor en el SDK para persistencia real en Desktop
tokenManager.setStorage(new DesktopStorageProvider());
