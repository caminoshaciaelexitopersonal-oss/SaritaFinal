import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import './services/storage';
import { LoginPage } from './pages/Login';
import { HomePage } from './pages/Home';
import { DashboardLayout } from './dashboard/DashboardLayout';
import { DashboardHome } from './dashboard/DashboardHome';
import { BusinessManager, BusinessSummary } from './dashboard/MiNegocio';
import { CustomersManager } from './dashboard/commercial/CustomersManager';
import { OpportunitiesManager } from './dashboard/commercial/OpportunitiesManager';
import { SalesManager } from './dashboard/commercial/SalesManager';
import { PromotionsManager } from './dashboard/commercial/PromotionsManager';
import { CommercialReports } from './dashboard/commercial/CommercialReports';
import { ArchiveDashboard } from './dashboard/archive/ArchiveDashboard';
import { DocumentsManager } from './dashboard/archive/DocumentsManager';
import { ArchiveActivityLog } from './dashboard/archive/ArchiveActivityLog';
import { OperationsDashboard } from './dashboard/operations/OperationsDashboard';
import { ToursManager } from './dashboard/operations/ToursManager';
import { BookingsCalendar } from './dashboard/operations/BookingsCalendar';
import { StaffManager } from './dashboard/operations/StaffManager';
import { ResourceScheduler } from './dashboard/operations/ResourceScheduler';
import { AccountingDashboard } from './dashboard/accounting/AccountingDashboard';
import { ChartOfAccounts } from './dashboard/accounting/ChartOfAccounts';
import { JournalEntries } from './dashboard/accounting/JournalEntries';
import { BalanceSheet, IncomeStatement } from './dashboard/accounting/FinancialStatements';
import { ReconciliationManager } from './dashboard/accounting/ReconciliationManager';
import { AccountingAuditLog } from './dashboard/accounting/AccountingAuditLog';
import { FinanceDashboard } from './dashboard/finance/FinanceDashboard';
import { WalletDashboard } from './dashboard/Wallet';
import { DeliveryManager } from './dashboard/Delivery';
import { AdminDashboard } from './admin/AdminDashboard';
import { TouristDashboard } from './dashboard/TouristDashboard';
import { CouncilDashboard } from './dashboard/CouncilDashboard';
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
                <Route path="negocio" element={<BusinessManager />}>
                  <Route index element={<BusinessSummary />} />
                  <Route path="clientes" element={<CustomersManager />} />
                  <Route path="oportunidades" element={<OpportunitiesManager />} />
                  <Route path="ventas" element={<SalesManager />} />
                  <Route path="promociones" element={<PromotionsManager />} />
                  <Route path="operaciones" element={<OperationsDashboard />} />
                  <Route path="archivo" element={<ArchiveDashboard />} />
                  <Route path="contabilidad" element={<AccountingDashboard />} />
                  <Route path="finanzas" element={<FinanceDashboard />} />
                  <Route path="reportes" element={<CommercialReports />} />
                </Route>
                <Route path="wallet" element={<WalletDashboard />} />
                <Route path="delivery" element={<DeliveryManager />} />
                <Route path="tourist" element={<TouristDashboard />} />
                <Route path="council" element={<CouncilDashboard />} />
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
