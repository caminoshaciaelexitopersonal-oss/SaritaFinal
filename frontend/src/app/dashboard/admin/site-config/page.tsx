import SiteConfigManager from '@/components/admin/SiteConfigManager';
import { AuthGuard } from '@/components/ui/AuthGuard';

const AdminSiteConfigPage = () => {
  return (
    <AuthGuard allowedRoles={['ADMIN']}>
      <SiteConfigManager />
    </AuthGuard>
  );
};

export default AdminSiteConfigPage;