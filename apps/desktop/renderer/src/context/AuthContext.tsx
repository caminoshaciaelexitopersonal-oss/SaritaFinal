import React, { createContext, useContext, useState, useEffect } from 'react';
import { tokenManager, User } from '@sarita/shared-sdk';
import { api } from '../services/api';

interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (credentials: any) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const initAuth = async () => {
      const token = await tokenManager.getToken();
      const userData = await tokenManager.getUserData();
      if (token && userData) {
        setUser(userData);
      }
      setLoading(false);
    };
    initAuth();
  }, []);

  const login = async (credentials: any) => {
    try {
      // Conexión real al endpoint de token del backend centralizado
      const response = await api.post('/token/', credentials);
      const { access, user: userData } = response.data;

      await tokenManager.setToken(access);
      await tokenManager.setUserData(userData);
      setUser(userData);
    } catch (error) {
      console.error('Error in desktop login:', error);
      throw error;
    }
  };

  const logout = () => {
    tokenManager.clearToken();
    tokenManager.clearUserData();
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth must be used within AuthProvider');
  return context;
};
