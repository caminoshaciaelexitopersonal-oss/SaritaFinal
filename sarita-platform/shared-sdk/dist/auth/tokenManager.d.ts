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
export declare class TokenManager {
    private static instance;
    private storage;
    private cachedToken;
    private constructor();
    static getInstance(): TokenManager;
    setStorage(provider: StorageProvider): void;
    setToken(token: string): Promise<void>;
    getToken(): Promise<string | null>;
    clearToken(): Promise<void>;
}
export declare const tokenManager: TokenManager;
