import ClienteManager from '@/components/prestador/ClienteManager';
import { AuthGuard } from '@/components/ui/AuthGuard';

const ClientesPage = () => {
  return (
    <AuthGuard allowedRoles={['PRESTADOR']}>
      <ClienteManager />
    </AuthGuard>
  );
};

export default ClientesPage;