"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.tokenManager = exports.TokenManager = void 0;
/**
 * Gestor de Tokens compartido.
 * Permite inyectar un proveedor de almacenamiento según el cliente (Web, Mobile, Desktop).
 */
class TokenManager {
    static instance;
    storage = null;
    cachedToken = null;
    constructor() { }
    static getInstance() {
        if (!TokenManager.instance) {
            TokenManager.instance = new TokenManager();
        }
        return TokenManager.instance;
    }
    setStorage(provider) {
        this.storage = provider;
    }
    async setToken(token) {
        this.cachedToken = token;
        if (this.storage) {
            await this.storage.setItem('sarita_auth_token', token);
        }
    }
    async getToken() {
        if (this.cachedToken)
            return this.cachedToken;
        if (this.storage) {
            this.cachedToken = await this.storage.getItem('sarita_auth_token');
        }
        return this.cachedToken;
    }
    async clearToken() {
        this.cachedToken = null;
        if (this.storage) {
            await this.storage.removeItem('sarita_auth_token');
        }
    }
}
exports.TokenManager = TokenManager;
exports.tokenManager = TokenManager.getInstance();
