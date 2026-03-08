import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import { LoginPage } from './pages/Login';
import { HomePage } from './pages/Home';
import { DashboardLayout } from './dashboard/DashboardLayout';
import { DashboardHome } from './dashboard/DashboardHome';
import { BusinessManager } from './dashboard/MiNegocio';
import { WalletDashboard } from './dashboard/Wallet';
import { DeliveryManager } from './dashboard/Delivery';
import { AdminDashboard } from './admin/AdminDashboard';
import './index.css';

const ProtectedRoute = ({ children }: { children: React.ReactNode }) => {
  const { user, loading } = useAuth();
  if (loading) return <div>Cargando...</div>;
  if (!user) return <Navigate to="/login" />;
  return <>{children}</>;
};

const App = () => (
  <BrowserRouter>
    <AuthProvider>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/dashboard/*" element={
          <ProtectedRoute>
            <DashboardLayout>
              <Routes>
                <Route path="home" element={<DashboardHome />} />
                <Route path="negocio" element={<BusinessManager />} />
                <Route path="wallet" element={<WalletDashboard />} />
                <Route path="delivery" element={<DeliveryManager />} />
                <Route path="admin" element={<AdminDashboard />} />
                <Route path="*" element={<Navigate to="home" />} />
              </Routes>
            </DashboardLayout>
          </ProtectedRoute>
        } />
        <Route path="/" element={<Navigate to="/login" />} />
      </Routes>
    </AuthProvider>
  </BrowserRouter>
);

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
