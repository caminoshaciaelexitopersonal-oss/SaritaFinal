import { StorageProvider, tokenManager, httpClient } from '@sarita/shared-sdk';
import * as SecureStore from 'expo-secure-store';
import { API_URL } from '../config/env';

/**
 * Proveedor de Almacenamiento Seguro para Mobile (Expo)
 */
class MobileStorageProvider implements StorageProvider {
  async getItem(key: string): Promise<string | null> {
    return await SecureStore.getItemAsync(key);
  }
  async setItem(key: string, value: string): Promise<void> {
    await SecureStore.setItemAsync(key, value);
  }
  async removeItem(key: string): Promise<void> {
    await SecureStore.deleteItemAsync(key);
  }
}

// Inyectar el proveedor en el SDK
tokenManager.setStorage(new MobileStorageProvider());

// Configurar la URL base del cliente HTTP del SDK de forma segura
httpClient.defaults.baseURL = `${API_URL}${API_V1_PREFIX}`;

export { httpClient as api };
