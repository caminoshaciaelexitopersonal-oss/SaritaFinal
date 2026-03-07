"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.httpClient = void 0;
const axios_1 = __importDefault(require("axios"));
const tokenManager_1 = require("../auth/tokenManager");
/**
 * Cliente HTTP estandarizado de SARITA.
 * Implementa interceptores para autenticación JWT y manejo de errores centralizado.
 */
exports.httpClient = axios_1.default.create({
    baseURL: process.env.API_URL || 'http://localhost:8000/api/v1',
    timeout: 10000,
});
exports.httpClient.interceptors.request.use(async (config) => {
    const token = await tokenManager_1.tokenManager.getToken();
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});
// Interceptor de respuesta para manejo de errores de clase mundial
exports.httpClient.interceptors.response.use((response) => response, (error) => {
    if (error.response?.status === 401) {
        console.warn('SARITA API: Sesión expirada o inválida. Limpiando token...');
        tokenManager_1.tokenManager.clearToken();
    }
    return Promise.reject(error);
});
exports.default = exports.httpClient;
