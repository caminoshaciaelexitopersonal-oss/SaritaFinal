import React, { createContext, useContext, useState, useEffect } from 'react';
import * as SecureStore from 'expo-secure-store';
import { api } from '../services/api';
import { User, tokenManager } from '@sarita/shared-sdk';

interface AuthContextData {
  user: User | null;
  loading: boolean;
  signIn: (credentials: any) => Promise<void>;
  signOut: () => Promise<void>;
}

const AuthContext = createContext<AuthContextData>({} as AuthContextData);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadStorageData() {
      const token = await tokenManager.getToken();
      const userData = await tokenManager.getUserData();

      if (token && userData) {
        setUser(userData);
      }
      setLoading(false);
    }

    loadStorageData();
  }, []);

  const signIn = async (credentials: any) => {
    try {
      const response = await api.post('/token/', credentials);
      const { access, user: userData } = response.data;

      // Usar el tokenManager del SDK para persistencia unificada
      await tokenManager.setToken(access);
      await tokenManager.setUserData(userData);

      setUser(userData);
    } catch (error) {
      console.error('Error in signIn:', error);
      throw error;
    }
  };

  const signOut = async () => {
    await tokenManager.clearToken();
    await tokenManager.clearUserData();
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, loading, signIn, signOut }}>
      {children}
    </AuthContext.Provider>
  );
};

export function useAuth() {
  return useContext(AuthContext);
}
