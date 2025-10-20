import ProductoManager from '@/components/prestador/ProductoManager';
import { AuthGuard } from '@/components/ui/AuthGuard';

const ProductosPage = () => {
  return (
    <AuthGuard allowedRoles={['PRESTADOR']}>
      <ProductoManager />
    </AuthGuard>
  );
};

export default ProductosPage;