import DashboardPrestador from '@/components/prestador/DashboardPrestador';
import { AuthGuard } from '@/components/ui/AuthGuard';

const PrestadorDashboardPage = () => {
  return (
    <AuthGuard allowedRoles={['PRESTADOR']}>
      <DashboardPrestador />
    </AuthGuard>
  );
};

export default PrestadorDashboardPage;