import UserManager from '@/components/admin/UserManager';
import { AuthGuard } from '@/components/ui/AuthGuard';

const AdminUsersPage = () => {
  return (
    <AuthGuard allowedRoles={['ADMIN']}>
      <UserManager />
    </AuthGuard>
  );
};

export default AdminUsersPage;