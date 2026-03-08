import React, { createContext, useContext, useState, useEffect } from 'react';
import { tokenManager, User } from '@sarita/shared-sdk';

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
      if (token) {
        // En una implementación real se llamaría a /me/
        setUser({ id: '1', email: 'admin@sarita.travel', first_name: 'Admin', last_name: 'SARITA', role: 'admin' });
      }
      setLoading(false);
    };
    initAuth();
  }, []);

  const login = async (credentials: any) => {
    // Simulación de login conectada al SDK en el futuro
    await tokenManager.setToken('fake-jwt-token');
    setUser({ id: '1', email: 'admin@sarita.travel', first_name: 'Admin', last_name: 'SARITA', role: 'admin' });
  };

  const logout = () => {
    tokenManager.clearToken();
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
