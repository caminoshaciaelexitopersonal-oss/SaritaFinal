/**
 * Interfaz de Almacenamiento Seguro (Persistencia Multiplataforma)
 */
export interface StorageProvider {
  getItem(key: string): Promise<string | null>;
  setItem(key: string, value: string): Promise<void>;
  removeItem(key: string): Promise<void>;
}

/**
 * Gestor de Tokens compartido.
 * Permite inyectar un proveedor de almacenamiento según el cliente (Web, Mobile, Desktop).
 */
export class TokenManager {
  private static instance: TokenManager;
  private storage: StorageProvider | null = null;
  private cachedToken: string | null = null;

  private constructor() {}

  public static getInstance(): TokenManager {
    if (!TokenManager.instance) {
      TokenManager.instance = new TokenManager();
    }
    return TokenManager.instance;
  }

  public setStorage(provider: StorageProvider) {
    this.storage = provider;
  }

  public async setToken(token: string): Promise<void> {
    this.cachedToken = token;
    if (this.storage) {
      await this.storage.setItem('sarita_auth_token', token);
    }
  }

  public async getToken(): Promise<string | null> {
    if (this.cachedToken) return this.cachedToken;
    if (this.storage) {
      this.cachedToken = await this.storage.getItem('sarita_auth_token');
    }
    return this.cachedToken;
  }

  public async clearToken(): Promise<void> {
    this.cachedToken = null;
    if (this.storage) {
      await this.storage.removeItem('sarita_auth_token');
    }
  }

  /**
   * Alias para compatibilidad hacia atrás
   */
  public async clear(): Promise<void> {
    return this.clearToken();
  }

  public async setUserData(user: any): Promise<void> {
    if (this.storage) {
      await this.storage.setItem('sarita_user_data', JSON.stringify(user));
    }
  }

  public async getUserData(): Promise<any | null> {
    if (this.storage) {
      const data = await this.storage.getItem('sarita_user_data');
      return data ? JSON.parse(data) : null;
    }
    return null;
  }

  public async clearUserData(): Promise<void> {
    if (this.storage) {
      await this.storage.removeItem('sarita_user_data');
    }
  }
}

export const tokenManager = TokenManager.getInstance();
